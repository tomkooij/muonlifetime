import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fit_func  = lambda x,a,b,c : a*np.exp(b*x)+c

if __name__=='__main__':
    # open .txt
    data = np.genfromtxt('Lifetime_hitdata.txt',delimiter=';')
    lifetime = data[:,4]

    plt.figure()
    plt.title('muon lifetime')
    plt.ylabel('counts')
    plt.xlabel('delta-t [ns]')

    # histogram
    n, bins, bla = plt.hist(lifetime, bins=np.arange(20.,1500.,20.), histtype='step')

    # Fit een dalende exponent
    initialguess = [100., -0.05, 0.]
    middle = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]
    c, cov = curve_fit(fit_func, middle, n, p0=initialguess)
    print "fit result: ",c

    # Levensduur = ln(2)/lambda
    muonlifetime = float(-1*np.log(2)/c[1])
    print "\nCalculated lifetime: %4.f ns." % muonlifetime

    # plot de gefitte functie ook in de grafiek
    xfit = np.array(middle)
    yfit = fit_func(xfit, c[0], c[1], c[2])
    plt.plot(xfit, yfit, 'r--')
    plt.legend(['fit lifetime = %4.f ns' % muonlifetime, 'data'])
    plt.show()
