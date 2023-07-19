def emist(trec, pc, clk):
    """
    Calculates the emission time of a satellite signal.

    Args:
        trec (float): Reception time in seconds of the day.
        pc (float): Code pseudorange observation from the receiver in meters.
        clk (ndarray): 10x2 matrix (or corresponding vector) with time tags (t) in the 1st column
                       and satellite clock corrections in seconds in the 2nd column.

    Returns:
        float: Emission time of the satellite signal in seconds of the day.
    """
    # m/s - speed of light
    c = 299792458
    
    # satellite clock error
    sce = lagrange(trec, clk)
    
    # The distance between t receiver reception and t satellite emission - delta_t
    delta_t = pc / c
    
    # Epoch free from satellite and receiver errors - tems
    tems = trec - delta_t - sce

    return tems
