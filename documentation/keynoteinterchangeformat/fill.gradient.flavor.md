# Fill.Gradient.Flavor

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A method for laying out a gradient’s stops over the area being filled.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Fill.Gradient.Flavor.linear | Fill.Gradient.Flavor.radial) Fill.Gradient.Flavor
```



**Allowed Types**: `Fill.Gradient.Flavor.linear`, `Fill.Gradient.Flavor.radial`

## Discussion

Each case’s value gives the geometry that positions the stops.

This value takes one of the following forms:

- `linear`: A gradient that varies along a straight line between its stops.
- `radial`: A gradient that spreads outward from a center point.

## Topics

### Objects
- [object Fill.Gradient.Flavor.Linear](./fill.gradient.flavor.linear.md)
  A gradient that lays out its stops along a straight line.
- [object Fill.Gradient.Flavor.Radial](./fill.gradient.flavor.radial.md)
  A gradient that spreads its stops outward from a center point, with a second point fixing the radius and the direction of the outer edge.
### Dictionaries
- [object Fill.Gradient.Flavor.linear](./fill.gradient.flavor/linear.md)
  A gradient that varies along a straight line between its stops.
- [object Fill.Gradient.Flavor.radial](./fill.gradient.flavor/radial.md)
  A gradient that spreads outward from a center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.gradient.flavor)*