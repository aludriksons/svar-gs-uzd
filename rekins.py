def cena(termins,rad1,rad2):
  if termins==1:
    k=rad2-rad1
    summa=k*0.20159
  elif termins==2:
    k=rad2-rad1
    summa=k*0.16961
  elif termins==3:
    k=rad2-rad1
    summa=k*0.16427
  else:
    k=rad2-rad1
    summa=k*0.15964
  return summa, k