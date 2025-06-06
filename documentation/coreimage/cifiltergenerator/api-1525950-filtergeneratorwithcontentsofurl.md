# filterGeneratorWithContentsOfURL:

**Framework**: Core Image  
**Kind**: clm

Creates and returns a filter generator object and initializes it with the contents of a filter generator file.

**Availability**:
- macOS 10.5+

## Declaration

```swift
+ (CIFilterGenerator *)filterGeneratorWithContentsOfURL:(NSURL *)aURL;
```

#### Return_value

A [`CIFilterGenerator`](cifiltergenerator.md) object;  returns `nil` if the file can’t be read.

## Parameters

- `aURL`: The location of a filter generator file.

## See Also

- [+ filterGenerator](cifiltergenerator/1525954-filtergenerator.md)
  Creates and returns an empty filter generator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1525950-filtergeneratorwithcontentsofurl)*