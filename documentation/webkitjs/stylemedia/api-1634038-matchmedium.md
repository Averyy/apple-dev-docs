# matchMedium

**Framework**: WebKit JS  
**Kind**: instm

Evaluates the given string as a media query and returns the result.

**Availability**:
- Safari Desktop 5.0+
- Safari Mobile 4.2+

## Declaration

```swift
boolean matchMedium(
    optional DOMString mediaquery
);
```

#### Return_value

`true` if the media query is logically true; otherwise, `false`.

#### Discussion

For example, `window.styleMedia.matchMedium("(color)")` returns `true` if the display device is a color device. You can also use this method to check whether the browser supports 3D transforms as follows:

```javascript
if ('styleMedia' in window && window.styleMedia.matchMedium("(-webkit-transform-3d)")) {
  // Insert 3D code here
}
```

Or check to see whether the browser supports animations as follows:

```javascript
if ('styleMedia' in window && window.styleMedia.matchMedium("(-webkit-animation)")) {
  // Insert animation code here
}
```

## Parameters

- `mediaquery`: The media query to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/stylemedia/1634038-matchmedium)*