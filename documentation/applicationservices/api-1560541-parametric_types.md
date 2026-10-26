# Parametric Types

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Specify a parametric curve type enumeration,

**Availability**:
- macOS 10.1+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [cmParametricType0](./api-1560541-parametric_types/cmparametrictype0.md)
   Y = X^gamma
- [cmParametricType1](./api-1560541-parametric_types/cmparametrictype1.md)
  Y = (aX+b)^gamma     [X>=-b/a],  Y = 0    [X<-b/a]
- [cmParametricType2](./api-1560541-parametric_types/cmparametrictype2.md)
  Y = (aX+b)^gamma + c [X>=-b/a],  Y = c    [X<-b/a]
- [cmParametricType3](./api-1560541-parametric_types/cmparametrictype3.md)
  Y = (aX+b)^gamma     [X>=d],     Y = cX   [X<d]
- [cmParametricType4](./api-1560541-parametric_types/cmparametrictype4.md)
  Y = (aX+b)^gamma + e [X>=d],     Y = cX+f [X<d]


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types)*