# IOUserVideoObjectPropertySelector

**Framework**: VideoDriverKit  
**Kind**: typealias

A four character code which, along with the scope and element, specifies a specific piece of information about a video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
typedef uint32_t IOUserVideoObjectPropertySelector;
```

#### Discussion

The property selector specifies the general classification of the property such as volume, stream format, or latency. Note that each class has a different set of selectors. A subclass inherits its superclass’s set of selectors, although it may not implement them all.

## See Also

- [PropertiesChanged](iouservideodriver/propertieschanged.md)
  This method informs the host when the state of an driver’s object changes.
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyselector)*