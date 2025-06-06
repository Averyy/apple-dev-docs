# StyleMedia

**Framework**: Webkitjs  
**Kind**: cl

The `StyleMedia` class provides a way to evaluate CSS media queries from JavaScript. You do not need to, nor should you, create instances of this class. You access the shared `StyleMedia` object using the window’s [`styleMedia`](domwindow/1632755-stylemedia.md) property.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 4.2+

## Declaration

```swift
interface StyleMedia
```

#### Overview

> **Note**: This class name changed from `Media` in iOS 4.2 and later.

This class name changed from `Media` in iOS 4.2 and later.

## Topics

### Get Properties
- [type](stylemedia/1634102-type.md)
  A string that represents the media type of the current view used for rendering the document. 
### Make Media Queries
- [matchMedium](stylemedia/1634038-matchmedium.md)
  Evaluates the given string as a media query and returns the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/stylemedia)*