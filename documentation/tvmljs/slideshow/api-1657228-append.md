# append

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Add additional images to a currently running slideshow.

**Availability**:
- tvOS 10.0+

## Declaration

```
void append(
    in Object imageRequests
);
```

## Discussion

The `imageRequests` parameter contains an array of image request objects that can have the following formatting:

- An array of URLs.
- A dictionary with two key-value pairs, `headers` and `urls`. `headers` provides a dictionary of headers that is included with all image requests. `urls` contains an array of URLs.

## Parameters

- `imageRequests`: An array of image request objects.

## See Also

### Creating and Modifying a Slideshow
- [dismiss](./api-1657241-dismiss.md)
  Dismisses a currently running slideshow.
- [start](./api-1657265-start.md)
  Starts a slideshow with the given set of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/slideshow/1657228-append)*