#
# This function will pull data from www.alphavantage.co
#
#
#


stock = function(ticker_sym,key){
    
    # Make API call
    URL = paste(c('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=',ticker_sym,'&outputsize=full&apikey=',key,'&datatype=csv'),collapse = '')
    DATA = read.csv(url(URL))
    
    #calculate daily return
    DATA = 
      DATA%>%
      mutate(return = ((close-open)/open)*100)
    
    #return the data
    return(DATA)
}
