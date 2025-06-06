# Parametric Types

**Framework**: Application Services

Specify a parametric curve type enumeration,

## Topics

### Constants
- [var cmParametricType0: Int](cmparametrictype0.md)
   Y = X^gamma
- [var cmParametricType1: Int](cmparametrictype1.md)
  Y = (aX+b)^gamma     [X>=-b/a],  Y = 0    [X<-b/a]
- [var cmParametricType2: Int](cmparametrictype2.md)
  Y = (aX+b)^gamma + c [X>=-b/a],  Y = c    [X<-b/a]
- [var cmParametricType3: Int](cmparametrictype3.md)
  Y = (aX+b)^gamma     [X>=d],     Y = cX   [X<d]
- [var cmParametricType4: Int](cmparametrictype4.md)
  Y = (aX+b)^gamma + e [X>=d],     Y = cX+f [X<d]


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560541-parametric_types)*