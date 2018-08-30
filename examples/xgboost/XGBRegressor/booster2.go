package model


func predict2(features []float64) float64 {
    if (features[2] < 0.5) || (features[2] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[0] < 0.5) || (features[0] == -1) {
                if (features[6] < 0.0760708675) || (features[6] == -1) {
                    if (features[16] < 0.32698375) || (features[16] == -1) {
                        if (features[7] < 0.268250227) || (features[7] == -1) {
                            if (features[5] < 0.360856116) || (features[5] == -1) {
                                return 0.552726686
                            } else {
                                return -3.35712743
                            }
                        } else {
                            return 3.59137011
                        }
                    } else {
                        if (features[14] < 0.838974714) || (features[14] == -1) {
                            if (features[14] < 0.442470878) || (features[14] == -1) {
                                return 6.50993109
                            } else {
                                return 2.97817874
                            }
                        } else {
                            if (features[3] < 0.68460989) || (features[3] == -1) {
                                return -1.5195111
                            } else {
                                return 0.495405883
                            }
                        }
                    }
                } else {
                    if (features[7] < 0.108870044) || (features[7] == -1) {
                        if (features[9] < 0.264320642) || (features[9] == -1) {
                            if (features[6] < 0.741639555) || (features[6] == -1) {
                                return 3.48238301
                            } else {
                                return 58.0834923
                            }
                        } else {
                            if (features[15] < 0.0908528864) || (features[15] == -1) {
                                return 3.46036792
                            } else {
                                return 65.4346848
                            }
                        }
                    } else {
                        if (features[16] < 0.594482124) || (features[16] == -1) {
                            if (features[7] < 0.711652517) || (features[7] == -1) {
                                return 41.8439522
                            } else {
                                return 20.5362568
                            }
                        } else {
                            if (features[15] < 0.559699059) || (features[15] == -1) {
                                return 27.8098278
                            } else {
                                return 7.9497261
                            }
                        }
                    }
                }
            } else {
                return 8.10288143
            }
        } else {
            return 1.1799258
        }
    } else {
        return 80.7237396
    }
}
