bmi=lambda w,h_cm : w/((h_cm/100)**2)
peter_w=81
peter_h_cm=182
peter_bmi= bmi(peter_w, peter_h_cm)
print("Peters BMi is ", round(peter_bmi,2))
