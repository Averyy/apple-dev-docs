# MPSMatrixRandomDistributionDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixRandomDistributionDescriptor : NSObject
```

## Topics

### Instance Properties
- [var distributionType: MPSMatrixRandomDistribution](mpsmatrixrandomdistributiondescriptor/3242857-distributiontype.md)
- [var maximum: Float](mpsmatrixrandomdistributiondescriptor/3242858-maximum.md)
- [var mean: Float](mpsmatrixrandomdistributiondescriptor/3242859-mean.md)
- [var minimum: Float](mpsmatrixrandomdistributiondescriptor/3242860-minimum.md)
- [var standardDeviation: Float](mpsmatrixrandomdistributiondescriptor/3242861-standarddeviation.md)
### Type Methods
- [class func `default`() -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/3242856-default.md)
- [class func normalDistributionDescriptor(withMean: Float, standardDeviation: Float) -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/3547979-normaldistributiondescriptor.md)
- [class func normalDistributionDescriptor(withMean: Float, standardDeviation: Float, minimum: Float, maximum: Float) -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/3547980-normaldistributiondescriptor.md)
- [class func uniformDistributionDescriptor(withMinimum: Float, maximum: Float) -> MPSMatrixRandomDistributionDescriptor](mpsmatrixrandomdistributiondescriptor/3242862-uniformdistributiondescriptor.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandomdistributiondescriptor)*