BLACK_S = function(){
  
  delta = as.numeric(readline(prompt = paste("What is delta, or continuous divident yeild? (%)",":")))
  r<- as.numeric(readline(prompt = paste("What is r? (%)",":")))
  sigma<- as.numeric(readline(prompt = paste("What is sigma? (%)",":")))
  
  time = as.numeric(readline(prompt = paste("What is T, or time in years?",":")))
  S = as.numeric(readline(prompt = paste("What is the stock price? (S)",":")))
  K = as.numeric(readline(prompt = paste("What is k? ($)",":")))
  
  delta = delta/100
  r = r/100
  sigma = sigma/100
  
  d1 = ((log(S/K)) + ((r-delta+.5*sigma^2)*time))
  d1= d1/(sigma*sqrt(time))
  nd1 = pnorm(d1,mean = 0,sd=1)
  
  d2 = d1 -sigma*sqrt(time)
  nd2 = pnorm(d2,mean = 0,sd=1)
  
  BS_CALL = S*exp(-delta*time)*nd1 - K*exp(-r*time)*nd2
  
  BS_PUT = BS_CALL + K*exp(-r*time) - S*exp(-delta*time)
  
  ####### GREEKS START HERE ##########
  
  DELTA_CALL = exp(-delta*(time))*pnorm(d1,mean = 0,sd = 1)
  DELTA_PUT = -exp(-delta*time)*pnorm(-d1,mean = 0,sd=1) 
  
  GAMMA_CALL = (exp(-delta*time)* dnorm(d1,mean = 0,sd=1))/(S*sigma*sqrt(time))
  GAMMA_PUT = GAMMA_CALL # WE CHANGED TO "DNORM" UNDER THE ASSUMPTION:
  # THE DERIVATIVITE OF STANDARD NORMAL CDF WAS TAKEN.
  
  THETA_CALL = delta*S*exp(-delta*(time))*pnorm(d1,mean = 0,sd=1) - r*K*exp(-r*(time))*pnorm(d2,mean = 0,sd=1) - ((K*exp(-r*(time))*dnorm(d2,mean = 0,sd=1)*sigma)/(2*sqrt(time)))         
  THETA_PUT = THETA_CALL + r*K*exp(-r*(time)) - delta * S*exp(-delta*(time))
  
  VEGA_CALL = S*exp(-delta*time)*dnorm(d1,mean = 0,sd =1)*sqrt(time)
  VEGA_PUT = VEGA_CALL
  
  RHO_CALL = time*K*exp(-r*time)*pnorm(d2,mean = 0,sd =1)
  RHO_PUT = -time*K*exp(-r*time)*pnorm(-d2,mean = 0,sd=1)
  
  PSI_CALL = -time*S*exp(-delta*time)*pnorm(d1,mean = 0,sd =1)
  PSI_PUT = time*S*exp(-delta*time)*pnorm(-d1,mean = 0,sd=1)
  
  ########## GREEKS END HERE ##########
  
  
  BS_CALL = round(BS_CALL, digits = 4)
  BS_PUT = round(BS_PUT, digits = 4)
  
  DELTA_CALL = round(DELTA_CALL, digits = 4)
  DELTA_PUT = round(DELTA_PUT, digits = 4)
  
  GAMMA_CALL = round(GAMMA_CALL, digits = 4)
  GAMMA_PUT = round(GAMMA_PUT, digits = 4)
  
  THETA_CALL = round(THETA_CALL, digits = 4)
  THETA_PUT = round(THETA_PUT, digits = 4)
  
  VEGA_CALL = round(VEGA_CALL, digits = 4)
  VEGA_PUT = round(VEGA_PUT, digits = 4)
  
  RHO_CALL = round(RHO_CALL, digits = 4)
  RHO_PUT = round(RHO_PUT, digits = 4)
  
  PSI_CALL = round(PSI_CALL, digits = 4)
  PSI_PUT = round(PSI_PUT, digits = 4)
  
  
  #info = matrix(c("Call Price",BS_CALL,"Put Price",BS_PUT,
  #                'Gamma Call',GAMMA_CALL,'Gamma Put',GAMMA_PUT,
  #                'Delta Call',DELTA_CALL,'Delta Put',DELTA_PUT,
  #                'Theta Call',THETA_CALL,'Theta Put',THETA_PUT,
  #                'Vega Call',VEGA_CALL,'Vega Put',VEGA_PUT,
  #                'Rho Call',RHO_CALL,'Rho Put',RHO_PUT,
  #                'Psi Call',PSI_CALL,'Psi Put',PSI_PUT
  #                
  #                ),ncol = 2,byrow = TRUE)
  
  info = matrix(c(BS_CALL,BS_PUT,
                  DELTA_CALL,DELTA_PUT,
                  GAMMA_CALL,GAMMA_PUT,
                  THETA_CALL,THETA_PUT,
                  VEGA_CALL,VEGA_PUT,
                  RHO_CALL,RHO_PUT,
                  PSI_CALL,PSI_PUT)
                ,ncol = 2,byrow = TRUE)
  colnames(info)=c('Call Option','Put Option')
  rownames(info)=c('Price','Delta','Gamma','Theta','Vega','Rho','Psi')
  info = data.frame(info)
  
  return(info)
}
