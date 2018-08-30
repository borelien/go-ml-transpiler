package model


func predict0(features []float64) float64 {
    if (features[2] < 0.5) || (features[2] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[0] < 0.5) || (features[0] == -1) {
                if (features[7] < 0.108870044) || (features[7] == -1) {
                    if (features[9] < 0.264320642) || (features[9] == -1) {
                        if (features[6] < 0.741639555) || (features[6] == -1) {
                            if (features[13] < 0.338543236) || (features[13] == -1) {
                                return 7.53046131
                            } else {
                                return 1.16959524
                            }
                        } else {
                            return 66.677475
                        }
                    } else {
                        if (features[15] < 0.0908528864) || (features[15] == -1) {
                            if (features[3] < 0.366575122) || (features[3] == -1) {
                                return 5.02030754
                            } else {
                                return 0.730997026
                            }
                        } else {
                            if (features[3] < 0.0536817461) || (features[3] == -1) {
                                return 0.730997026
                            } else {
                                return 79.6467667
                            }
                        }
                    }
                } else {
                    if (features[16] < 0.594482124) || (features[16] == -1) {
                        if (features[7] < 0.711652517) || (features[7] == -1) {
                            if (features[6] < 0.104887083) || (features[6] == -1) {
                                return 5.6051054
                            } else {
                                return 52.235836
                            }
                        } else {
                            if (features[17] < 0.630156219) || (features[17] == -1) {
                                return 35.6895027
                            } else {
                                return 9.78621387
                            }
                        }
                    } else {
                        if (features[15] < 0.559699059) || (features[15] == -1) {
                            if (features[14] < 0.281556785) || (features[14] == -1) {
                                return 5.36788464
                            } else {
                                return 40.2028084
                            }
                        } else {
                            if (features[11] < 0.0317210704) || (features[11] == -1) {
                                return 66.677475
                            } else {
                                return 4.85689306
                            }
                        }
                    }
                }
            } else {
                return 9.99302959
            }
        } else {
            return 1.45519412
        }
    } else {
        return 99.5574265
    }
}
