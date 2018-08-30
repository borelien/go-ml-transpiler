package model


func predict0(features []float64) float64 {
    if (features[0] < 0.5) || (features[0] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[7] < 0.941666901) || (features[7] == -1) {
                if (features[13] < 0.105796114) || (features[13] == -1) {
                    return -0.114391111
                } else {
                    if (features[6] < 0.142166018) || (features[6] == -1) {
                        return -0.177215144
                    } else {
                        if (features[17] < 0.834355593) || (features[17] == -1) {
                            if (features[13] < 0.723351836) || (features[13] == -1) {
                                return -0.600997388
                            } else {
                                return -0.194630831
                            }
                        } else {
                            return -0.188191846
                        }
                    }
                }
            } else {
                return -0.0265486538
            }
        } else {
            return -0.950641453
        }
    } else {
        return 0.105527639
    }
}
