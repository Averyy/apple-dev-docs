# resumeTime

**Framework**: TVMLKit JS  
**Kind**: instp

The number of seconds from the beginning of the item at which the item begins playing.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute int resumeTime;
```

#### Discussion

Use this property to begin playing a media item at a time other than at the beginning of the item. If this property contains anything other than 0, the player displays “Resume” instead of “Play from beginning” on playback.

## See Also

- [highlightGroups](mediaitem/1627413-highlightgroups.md)
  An array of highlight groups, with each group containing a list of highlights.
- [interstitials](mediaitem/1627341-interstitials.md)
  An array of `interstitial` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/mediaitem/1627400-resumetime)*