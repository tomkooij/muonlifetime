import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fit_func  = lambda x,a,b : a*np.exp(b*x)

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
    initialguess = [100., -0.05]
    middle = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]
    c, cov = curve_fit(fit_func, middle, n, p0=initialguess)
    print "fit result: ",c

    # Levensduur = ln(2)/lambda
    muonlifetime = float(-1/c[1])
    print "\nCalculated lifetime: %4.f ns." % muonlifetime
    print "\nError (measured/real liftime ) = %2.2f" % float(2196./muonlifetime)
    # plot de gefitte functie ook in de grafiek
    xfit = np.array(middle)
    yfit = fit_func(xfit, c[0], c[1])
    plt.plot(xfit, yfit, 'r--')
    plt.legend(['fit lifetime = %4.f ns' % muonlifetime, 'data'])
    plt.show()
