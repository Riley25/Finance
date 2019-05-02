#
#
# AUTHOR: R.N.H.
#
#
#



BOND = function(){
  fv<- as.numeric(readline(prompt = paste("What is the Face Value of the Bond? ($)",":")))
  yr<- as.numeric(readline(prompt = paste("How many years will the bond last untill maturity?",":")))
  m <- as.numeric(readline(prompt = paste("How many compounding periods per year?",":")))
  c <- as.numeric(readline(prompt = paste("What is the coupon rate? (%)",":")))
  y <- as.numeric(readline(prompt = paste("What is the annulized yeild to maturity? (%)" ,":")))
  
  c=c/100
  y=y/100
  I = yr*m
  C = (c/m)*fv
  Y = y/m
  
  b=matrix(c(rep(NA,I)),ncol = 1)
  for (i in 1:I){
    b[i,]=((C)/(1+Y)^i)      
  }
  b= sum(b) + fv/((1+Y)^I)   
  
  
  MD=matrix(c(rep(NA,I)),ncol = 1)
  for (i in 1:I){
    MD[i,]=((i*C)/(m*(1+Y)^i))      #BY THM (7.11) PG. 213
  }
  MD= sum(MD) 
  MD = MD + (I*fv)/(m*(1+Y)^I)
  MD= (1/b)*MD
  
  
  PVBP=matrix(c(rep(NA,I)),ncol = 1)
  for (i in 1:I){
    PVBP[i,]=((i*C)/(m*(1+Y)^i))      #BY THM (7.11) PG. 213
  }
  PVBP= sum(PVBP) 
  PVBP = PVBP + (I*fv)/(m*(1+Y)^I)
  PVBP= (-1/1+Y)*PVBP
  PVBP = PVBP/10000
  
  CONVEX = matrix(c(rep(NA,I)), ncol = 1)
  for(i in 1:I){
    CONVEX[i,] = (i*(i+1)/m^2) * (C/(1+Y)^(i+2))}
  CONVEX = sum(CONVEX)
  CONVEX = CONVEX + (I*(I+1)/m^2) * fv/(1+Y)^(I+2)
  CONVEX = CONVEX * (1/b)
  
  PVBP = round(PVBP,digits = 4)
  b = round(b,digits = 3)
  MD = round(MD,digits = 3)
  CONVEX = round(CONVEX, digits = 3)
  
  x = "The name is Bond,"
  y = "JAMES BOND"
  info=matrix(c('Price','PVBP','Duration','Convexity',x,
                paste("$",b),PVBP,paste(MD, 'Years'),CONVEX,y),nrow = 5, byrow = FALSE)
  info=data.frame(info)
  colnames(info) = c('Variable','Value')
  
  return(info)
  
}

BOND_A = BOND()
1000
20
4
4
5
BOND_A
