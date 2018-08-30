package model


func predict1(features []float64) float64 {
    if (features[2] < 0.5) || (features[2] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[0] < 0.5) || (features[0] == -1) {
                if (features[7] < 0.108870044) || (features[7] == -1) {
                    if (features[9] < 0.264320642) || (features[9] == -1) {
                        if (features[6] < 0.741639555) || (features[6] == -1) {
                            if (features[13] < 0.338543236) || (features[13] == -1) {
                                return 6.96567678
                            } else {
                                return 1.07602775
                            }
                        } else {
                            return 62.2323074
                        }
                    } else {
                        if (features[15] < 0.0908528864) || (features[15] == -1) {
                            if (features[3] < 0.366575122) || (features[3] == -1) {
                                return 4.76929235
                            } else {
                                return 0.694447219
                            }
                        } else {
                            if (features[9] < 0.922377348) || (features[9] == -1) {
                                return 72.3714905
                            } else {
                                return -3.25134134
                            }
                        }
                    }
                } else {
                    if (features[14] < 0.877792954) || (features[14] == -1) {
                        if (features[16] < 0.594482124) || (features[16] == -1) {
                            if (features[7] < 0.711652517) || (features[7] == -1) {
                                return 46.916111
                            } else {
                                return 24.1145916
                            }
                        } else {
                            if (features[15] < 0.559699059) || (features[15] == -1) {
                                return 29.9923706
                            } else {
                                return 9.65826797
                            }
                        }
                    } else {
                        if (features[6] < 0.872805834) || (features[6] == -1) {
                            if (features[14] < 0.94291389) || (features[14] == -1) {
                                return -0.145070225
                            } else {
                                return 4.8073535
                            }
                        } else {
                            if (features[3] < 0.788281798) || (features[3] == -1) {
                                return 63.1950874
                            } else {
                                return 0.808762372
                            }
                        }
                    }
                }
            } else {
                return 8.99846268
            }
        } else {
            return 1.31035149
        }
    } else {
        return 89.6473465
    }
}
