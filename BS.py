#
# PRO: BS.py
#
# PURPOSE: Use Black-Scholes European price equation to price call and put option based upon required inputs (S, K, sigma, delta, r, time to maturity (years))
#
# DATE: 2/12/2022
#
# AUTHOR: R.H.
#

import pandas as pd

import math
import numpy as np
from scipy.stats import norm
import os 

# Where am I?
print(os.getcwd())


def BS(S, K, sigma, delta, r, time):
  d1 = ((np.log(S/K)) + (((r-delta)+.5*sigma*sigma)*time))
  d1= d1/(sigma*math.sqrt(time))
  nd1 = norm.cdf(d1,loc=0, scale=1)

  d2 = d1 -sigma*math.sqrt(time)
  nd2 = norm.cdf(d2,loc=0, scale=1)


  BS_CALL = S*np.exp(-delta*time)*nd1 - K*np.exp(-r*time)*nd2  
  BS_PUT = BS_CALL + K*np.exp(-r*time) - S*np.exp(-delta*time)

  BS_CALL = round(BS_CALL, ndigits = 4)
  BS_PUT =  round(BS_PUT,  ndigits = 4)

  ####### GREEKS START HERE ##########
  DELTA_CALL = np.exp(-delta*(time))*norm.cdf(d1,loc=0, scale=1)
  DELTA_PUT = -np.exp(-delta*time)*norm.cdf(-d1, loc=0, scale=1) 
  
  GAMMA_CALL = (np.exp(-delta*time)* norm.pdf(d1, loc = 0, scale = 1))/(S*sigma*np.sqrt(time))
  GAMMA_PUT = GAMMA_CALL 
  
  THETA_CALL = delta*S*np.exp(-delta*(time))*norm.cdf(d1,loc = 0, scale = 1) - r*K*np.exp(-r*(time))*norm.cdf(d2,loc = 0,scale=1) - ((K*np.exp(-r*(time))*norm.pdf(d2,loc = 0,scale=1)*sigma)/(2*np.sqrt(time)))         
  THETA_PUT = THETA_CALL + r*K*np.exp(-r*(time)) - delta * S*np.exp(-delta*(time))
  
  VEGA_CALL = S*np.exp(-delta*time)*norm.pdf(d1,loc = 0,scale =1)*np.sqrt(time)
  VEGA_PUT = VEGA_CALL
  
  RHO_CALL = time*K*np.exp(-r*time)*norm.cdf(d2,loc = 0,scale =1)
  RHO_PUT = -time*K*np.exp(-r*time)*norm.cdf(-d2, loc = 0, scale=1)
  
  PSI_CALL = -time*S*np.exp(-delta*time)*norm.cdf(d1, loc = 0, scale =1)
  PSI_PUT = time*S*np.exp(-delta*time)*norm.cdf(-d1,loc = 0, scale=1)
  ########## GREEKS END HERE ##########

  d = {'CALL':[BS_CALL, DELTA_CALL, GAMMA_CALL, THETA_CALL, VEGA_CALL, RHO_CALL, PSI_CALL], 
       'PUT' :[BS_PUT,  DELTA_PUT, GAMMA_PUT, THETA_PUT, VEGA_PUT, RHO_PUT, PSI_PUT]}
  df = pd.DataFrame(data=d, index=['Price', 'Delta', 'Gamma', 'Theta', 'Vega', 'Rho', 'Psi'])

  return(df)

def BS_PRICE(S, K, sigma, delta, r, time):
  d1 = ((np.log(S/K)) + (((r-delta)+.5*sigma*sigma)*time))
  d1= d1/(sigma*math.sqrt(time))
  nd1 = norm.cdf(d1,loc=0, scale=1)

  d2 = d1 -sigma*math.sqrt(time)
  nd2 = norm.cdf(d2,loc=0, scale=1)


  BS_CALL = S*np.exp(-delta*time)*nd1 - K*np.exp(-r*time)*nd2  
  BS_PUT = BS_CALL + K*np.exp(-r*time) - S*np.exp(-delta*time)
  return(BS_CALL, BS_PUT)




