# Resource

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The data used for image, movie, and audio media, and for image fills and image bullets.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Resource.base64_encoded | Resource.indirect) Resource
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)



**Allowed Types**: `Resource.base64_encoded`, `Resource.indirect`

## Discussion

Resources can be carried inline (`base64_encoded`), which makes the JSON self-contained, or refer to files stored alongside the JSON in the archive (`indirect`), which keeps large assets out of the JSON but can be read only when those files are present. What happens when bytes can’t be read (an `indirect` name that matches no file, or a `base64_encoded` string that isn’t valid Base64) depends on where the resource is used. An image, movie, or audio object whose media can’t be read is dropped with a warning, though a `Movie.poster_image` that can’t be read doesn’t drop the movie. Such an object placed inline in the text of a text box or shape removes the whole text box or shape, including all of its text, and so does an image bullet in that text. An image fill in a `SlideLayout.background` removes that whole layout, and one anywhere else is left out. An image bullet or such an object in a slide’s presenter notes (`Slide.note`), or an image bullet in a list style in `Presentation.stylesheet`, stops the document from loading.

This value takes one of the following forms:

- `base64_encoded`: Data carried inline in the resource.
- `indirect`: Data stored in a separate file, identified by name rather than carried in the resource.

## Topics

### Objects
- [object Resource.Base64EncodedResource](./resource.base64encodedresource.md)
  A resource whose bytes are carried as Base64 in the resource itself, so the JSON needs no companion files.
- [object Resource.IndirectResource](./resource.indirectresource.md)
  A resource whose bytes are stored in a separate file rather than in the JSON.
- [object Resource.PremiumResourceInfo](./resource.premiumresourceinfo.md)
  Additional metadata that marks a resource as premium content that the reader originally sourced from the content hub.
### Dictionaries
- [object Resource.base64_encoded](./resource/base64_encoded.md)
  Data carried inline in the resource.
- [object Resource.indirect](./resource/indirect.md)
  Data stored in a separate file, identified by name rather than carried in the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/resource)*