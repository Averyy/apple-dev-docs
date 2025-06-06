# start

**Framework**: TVMLKit JS  
**Kind**: instm

Starts a slideshow with the given set of images.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
void start(
    in Object imageRequests, 
    in Object options, 
    in Function exitCB
);
```

#### Discussion

When a new slideshow beings using the `start` function, if there is a currently running slideshow, that slideshow is dismissed. The `imageRequests` parameter contains an array of image request objects that can have the following formatting:

- An array of URLs.
- A dictionary with two key-value pairs, `headers` and `urls`. `headers` provides a dictionary of headers that is included with all image requests. `urls` contains an array of URLs.

If the `showSettings` key in the `options` parameter is set to `true` or `1`, the user will be asked to pick a theme before the slideshow begins. [`Listing 1`](slideshow/1657265-start#1943543.md) shows an example of a simple slideshow that is created with two images.

```javascript
function mySlideshow() {
   var images = ['path to image', 'path to image'];
   Slideshow.start(images, { 'showSettings': '0' });
}
```

## Parameters

- `imageRequests`: An array of image request objects.
- `options`: An optional set of options that modify the slideshow. If no options are specified, a default of   or  is used.
- `exitCB`: An optional callback function that is called when the slideshow is dismissed. If this parameter is not specified, the page on top of the navigation stack is displayed.

## See Also

- [append](slideshow/1657228-append.md)
  Add additional images to a currently running slideshow.
- [dismiss](slideshow/1657241-dismiss.md)
  Dismisses a currently running slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/slideshow/1657265-start)*