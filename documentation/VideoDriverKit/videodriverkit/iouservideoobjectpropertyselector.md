# IOUserVideoObjectPropertySelector

**Framework**: VideoDriverKit  
**Kind**: typealias

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
typedef uint32_t IOUserVideoObjectPropertySelector;
```

#### Discussion

An IOUserVideoObjectPropertySelector is a four char code that identifies, along with the IOUserVideoObjectPropertyScope and IOUserVideoObjectPropertyElement, a specific piece of information about an IOUserVideoObject.

The property selector specifies the general classification of the property such as volume, stream format, latency, etc. Note that each class has a different set of selectors. A subclass inherits its super class’s set of selectors, although it may not implement them all.

## See Also

- [PropertiesChanged](iouservideodriver/propertieschanged.md)
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyselector)*