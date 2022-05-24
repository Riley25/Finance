def GBM_FAST(mu, dt, time, So, n_lines, vol):
    #mu = .05
    #dt = (1/252)

    n = int(252 * time)
    #So = 50
    #n_lines = 10000

    #K = 60
    #H = 55
    sigma = np.array([vol]*n_lines)

    S = np.exp( (mu - sigma ** 2 / 2) * dt + sigma * np.random.normal(0, np.sqrt(dt), size=(len(sigma), n)).T )
    S = np.vstack([np.ones(len(sigma)), S])
    S = So * S.cumprod(axis=0)
    return(S)


# Step 1. Generate Terminal Stock Price 
S = GBM_FAST(mu, dt, time, So, n_lines, vol)

n_row, n_col = S.shape
terminal_prices = (S[(n_row-1)][:])
l = len(terminal_prices)


# Step 2. Apply the unbiased estimator
option_payoff = np.where(terminal_prices < K , (K-terminal_prices), 0.0 )
option_payoff = option_payoff * np_prob(vol,  time, H,  So, terminal_prices) 

price = np.power(np.average(option_payoff) , np.exp(-r*time))
print(price)



with plt.style.context('science'):
    fig, ax = plt.subplots(figsize=(3.75,3.25))
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    ax.yaxis.labelpad = 27
    plt.plot(time_steps, prices)

    plt.ylabel('Option \n Price $(\$)$', rotation = 'horizontal', fontsize = 14)
    plt.xlabel('Number of Monte Carlo Simulations', fontsize = 14)
    plt.title('Up-and-Out Put Option (UOP)', fontsize = 14)
    #plt.tight_layout()
    #plt.xlim(2000, np.max(time_steps))
    plt.savefig('plots/UOP_MC_500.jpg', dpi = 450)
    plt.show()



