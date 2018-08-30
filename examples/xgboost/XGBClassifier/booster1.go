package model


func predict1(features []float64) float64 {
    if (features[0] < 0.5) || (features[0] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[17] < 0.0454911441) || (features[17] == -1) {
                return 0.0167547371
            } else {
                if (features[7] < 0.926903129) || (features[7] == -1) {
                    if (features[9] < 0.0303293802) || (features[9] == -1) {
                        return -0.0400148854
                    } else {
                        if (features[7] < 0.0570837371) || (features[7] == -1) {
                            return -0.080148682
                        } else {
                            if (features[3] < 0.87570703) || (features[3] == -1) {
                                return -0.365225285
                            } else {
                                return -0.160631925
                            }
                        }
                    }
                } else {
                    return -0.0501447804
                }
            }
        } else {
            return -0.436093569
        }
    } else {
        return 0.104004852
    }
}
