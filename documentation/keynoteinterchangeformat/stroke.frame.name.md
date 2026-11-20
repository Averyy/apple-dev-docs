# Stroke.Frame.Name

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The name of the picture frame that Keynote uses to draw the border.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Stroke.Frame.Name
```

## Discussion

This frame is one of the artworks that Keynote ships. Only the frame listed here can be written, so when an object has any other frame, Keynote writes it with no border. If a frame of the given name can’t be found, the stroke is skipped rather than being replaced with a line, leaving the object unframed.

This value takes one of the following forms:

- `antique`
- `crayon_line`
- `formal_inset`
- `formal_shadow`
- `graph_paper`
- `headlines`
- `jet_set`
- `photo_portfolio1`: The picture frame shown in Keynote as “Photo portfolio.”
- `portfolio_inset`
- `pushpin`
- `renaissance1`: The picture frame shown in Keynote as Renaissance.
- `scrapbook2b`: The picture frame shown in Keynote as Scrapbook 2.
- `storyboard`
- `vintage_inset`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stroke.frame.name)*