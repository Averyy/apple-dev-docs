# MPSNNDefaultPadding

**Framework**: Metal Performance Shaders  
**Kind**: cl

A class that provides predefined padding policies for common tasks.    

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNDefaultPadding : NSObject
```

## Topics

### Initializers
- [init(method: MPSNNPaddingMethod)](mpsnndefaultpadding/2867160-init.md)
- [struct MPSNNPaddingMethod](mpsnnpaddingmethod.md)
  Options that define a graph's padding. 
### Instance Methods
- [func label() -> String](mpsnndefaultpadding/2889871-label.md)
### Type Methods
- [class func forTensorflowAveragePooling() -> Self](mpsnndefaultpadding/2867164-fortensorflowaveragepooling.md)
- [class func forTensorflowAveragePoolingValidOnly() -> Self](mpsnndefaultpadding/2947962-fortensorflowaveragepoolingvalid.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [MPSNNPadding](mpsnnpadding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnndefaultpadding)*