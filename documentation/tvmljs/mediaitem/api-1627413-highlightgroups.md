# highlightGroups

**Framework**: TVMLKit JS  
**Kind**: instp

An array of highlight groups, with each group containing a list of highlights.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute Array highlightGroups;
```

#### Discussion

The `highlightGroups` property enables you to show several groups of highlights from a stream. Each highlight group in the array contains a list of highlights. Each highlight is an object with the following properties: `description`, `duration`, `imageURL`, `name`, and `starttime`. Highlight objects are ad-hoc JSON objects and there are no explicit classes for these types.

A good way to envision how the `highlightGroups` property works is to think of a video of a baseball game. During the game, several home runs are hit. You can create a highlight group containing the video for each of these highlights and put the highlight group into the `highlightGroups` property. [`Listing 1`](mediaitem/1627413-highlightgroups#1943542.md) shows a complete example of how to set up a highlight group.

```javascript
var baseURL;
 
App.onLaunch = function(options) {
    baseURL = options.BASEURL;
    var documentPath = "path to file on server/baseball.m3u8";
    var videourl = baseURL + documentPath;
 
    var singleVideo = new MediaItem('video', videourl);
    var highlights = [{
        name: "Home Runs",
        highlights: [{
            name: "Johnny Appleseed 1st inning",
            description: "Johnny's 1st Homerun",
            starttime: 10,
            duration: 10,
            imageURL: "path to server/images/Car_Movie_90x90_A.png"
            },
        {
            name: "Johnny Appleseed 5th inning",
            description: "Johnny's 2nd Homerun",
            starttime: 60,
            duration: 10,
            imageURL: "path to server/images/Car_Movie_90x90_B.png"
            }
        ]
    }];
    singleVideo.highlightGroups = highlights;
    var videoList = new Playlist();
    videoList.push(singleVideo);
    var myPlayer = new Player();
    myPlayer.playlist = videoList;
    myPlayer.play();
}
 
App.onExit = function() {
    console.log("exited");
}
```

> **Note**: You can only have one set of highlights associated with a media item.

## See Also

- [interstitials](mediaitem/1627341-interstitials.md)
  An array of `interstitial` objects.
- [resumeTime](mediaitem/1627400-resumetime.md)
  The number of seconds from the beginning of the item at which the item begins playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/mediaitem/1627413-highlightgroups)*