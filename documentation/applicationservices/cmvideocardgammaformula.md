# CMVideoCardGammaFormula

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMVideoCardGammaFormula {
    ...
} CMVideoCardGammaFormula;
```

#### Overview

The ColorSync Manager defines the `CMVideoCardGammaFormula` data structure to specify video card gamma data by providing three values each for red, blue and green gamma. The values represent the actual gamma, the minimum gamma, and the maximum gamma for each color. Specifying video gamma information by formula takes less space than specifying it with a table, but the results may be less precise. 

## Topics

### Instance Properties
- [blueGamma](./cmvideocardgammaformula/api-1560125-bluegamma.md)
  The gamma value for blue. It must be greater than 0.0.
- [blueMax](./cmvideocardgammaformula/api-1560504-bluemax.md)
  The maximum gamma value for blue. It must be greater than 0.0 and less than 1.0.
- [blueMin](./cmvideocardgammaformula/api-1560213-bluemin.md)
  The minimum gamma value for blue. It must be greater than 0.0 and less than 1.0.
- [greenGamma](./cmvideocardgammaformula/api-1560602-greengamma.md)
  The gamma value for green. It must be greater than 0.0.
- [greenMax](./cmvideocardgammaformula/api-1560457-greenmax.md)
  The maximum gamma value for green. It must be greater than 0.0 and less than 1.0.
- [greenMin](./cmvideocardgammaformula/api-1560184-greenmin.md)
  The minimum gamma value for green. It must be greater than 0.0 and less than 1.0.
- [redGamma](./cmvideocardgammaformula/api-1560204-redgamma.md)
  The gamma value for red. It must be greater than 0.0.
- [redMax](./cmvideocardgammaformula/api-1560106-redmax.md)
  The maximum gamma value for red. It must be greater than 0.0 and less than 1.0.
- [redMin](./cmvideocardgammaformula/api-1560287-redmin.md)
  The minimum gamma value for red. It must be greater than 0.0 and less than 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmvideocardgammaformula)*