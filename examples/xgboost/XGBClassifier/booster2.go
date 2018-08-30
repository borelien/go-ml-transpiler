package model


func predict2(features []float64) float64 {
    if (features[0] < 0.5) || (features[0] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[17] < 0.0454911441) || (features[17] == -1) {
                return 0.0159571599
            } else {
                if (features[11] < 0.241154373) || (features[11] == -1) {
                    return -0.321541667
                } else {
                    if (features[7] < 0.891868591) || (features[7] == -1) {
                        if (features[14] < 0.321717471) || (features[14] == -1) {
                            if (features[3] < 0.251218945) || (features[3] == -1) {
                                return 0.0703224316
                            } else {
                                return -0.143259436
                            }
                        } else {
                            if (features[11] < 0.35271138) || (features[11] == -1) {
                                return -0.0646967366
                            } else {
                                return -0.274604678
                            }
                        }
                    } else {
                        return 0.0131435711
                    }
                }
            }
        } else {
            return -0.317927688
        }
    } else {
        return 0.102569357
    }
}
