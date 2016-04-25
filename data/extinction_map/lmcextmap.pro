pro lmcextmap, ra, dec, evi, SIGMA=sigma, INT_EVI=int_evi, NSTARS=nstars, SILENT=silent

;+
; NAME:
;      LMCEXTMAP
; PURPOSE:
;      Return E(V-I) and associated quantities in the Large Magellanic Cloud.
;      Derived using OGLE-III RR Lyr stars by Pejcha & Stanek (2009). If you
;      make use of this map please cite our paper.
;      The area covered is approximately 65 deg < RA < 97 deg and 
; INPUTS:
;       ra:     Right ascension (J2000) in decimal degrees. Scalar.
;       dec:    Declination (J2000) in decimal degrees. Scalar.
; OUTPUTS:
;       evi:    E(V-I). You can get A_I (extinction in I band) by multiplying this
;               value by 1.1 (see our paper for details).
; EXAMPLE:
;       lmcextmap, 86, -69, evi, sigma=sigma, int_evi=int_evi, nstars=nstars

; MODIFICATION HISTORY:
;        May 19 2009: created
;-



restore, filename='extmap.sav'




x = (ra-80.35)*cos(dec*!PI/180.)
y = dec+69.68

intj = floor((x-minx)/binx)
intk = floor((y-miny)/biny)

conti = 1


if ((intj lt 0) or (intj ge 49)) then begin
	print, "Right ascension is out of range - outside covered area of LMC"
	conti = 0
endif
if ((intk lt 0) or (intk ge 34)) then begin 
	print, "Declination is out of range - outside covered area of LMC"
	conti = 0
endif


if (conti ge 1) then begin
if (extmapflag[intj,intk] lt 2) then begin
	print, "There are not enough stars in the pixel (less than 2)"
	conti = 0
endif
endif

if (conti ge 1) then begin

	evi = extmap[intj,intk]/1.1	
	sigma = extmapdev[intj,intk]/1.1
	nstars = extmapflag[intj,intk]
	int_evi = (extmapdista[intj,intk]-extmapclose[intj,intk])/1.1

	if not(keyword_set(silent)) then begin
		print, "E(V-I) = ", string(extmap[intj,intk]/1.1,format='(F6.3)'), " mag"
		print, "with standard deviation of ", string(sigma, format='(F6.3)'), " mag. Computed from ", string(nstars,format='(I3)'), " stars."
		print, "I band extinction is ", string(extmap[intj,intk],format='(F6.3)')," mag"
		print, "Difference in E(V-I) between closer and more distant stars in pixel is ", string( int_evi,format='(F6.3)'), " mag."
		if (nstars lt 4) then print, "There are less than 4 stars in pixel. Internal reddening wasn't computed." else begin
			if (int_evi le 0.06) then print, "Warning, value of internal reddening is lower than 0.06 mag and therefore consistent with zero!"
		endelse
	endif
endif

end
