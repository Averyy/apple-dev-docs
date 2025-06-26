# Enhancing the audio experience for Petite Asteroids

**Framework**: visionOS

Elevate the game’s immersive experience using RealityKit audio.

**Availability**:
- visionOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

Petite Asteroids is a video game that tells the story of a lost chondrite as she collects her missing rock friends in a beautifully rendered environment.

![A screenshot of a towering butte presented in a volume within a mixed reality space running inside the visionOS simulator.](https://docs-assets.developer.apple.com/published/5c5cbc2b0a27d9ff68fcc88012c36f5b/petite-asteroids-overview%403x.png)

With this sample project, you can learn how to design sound for your 3D app by leveraging various RealityKit audio components and APIs.

#### Load Audio Assets in the Scene

In Petite Asteroids, the system accumulates collision sounds into a Swift list, and then passes the sounds into the initializer, [`init(_:)`](https://developer.apple.com/documentation/RealityKit/AudioFileGroupResource/init(_:)), for an `AudioFileGroupResource`. On startup, the app loads audio files into the scene using the `AudioResourcesComponent`. This componentʼs load function then caches the `AudioResource` using an `AudioLibraryComponent` for retrieval by name later in the app code. The app also adds other sounds, such as music and environmental ambiences, into the `AudioResourcesComponent`, in addition to the collision sounds, for later use.

#### Understand How Collision Audio Works

In Petite Asteroids, the audio system has multiple types of collision sounds. These sounds play depending on the [`CollisionEvents`](https://developer.apple.com/documentation/RealityKit/CollisionEvents) of their respective component. These events govern when and how to play the audio accordingly. The information that the system receives from the physics and collision events determines the loudness of the audio playback.

The physics event calculates the velocity of the character or if the character stops jumping, which changes the nature of the audio playback. The collision event provides information on the [`impulse`](https://developer.apple.com/documentation/RealityKit/CollisionEvents/Began/impulse), which is directly proportional to the loudness of the audio playback. When the character jumps or falls off of the butte, she lands on a virtual surface. The app plays a sound whenever the character collides with a virtual surface.

This sample shows how to handle collision events, play a sound upon collision, and track the collision entity throughout events.

```swift
import RealityKit

class GameMovementSystem: System {
    var subscriptions: [AnyCancellable] = .init()

    required init(scene: RealityKit.Scene) {
    // Subscribe to the CollisionEvents and connect to class methods.
    scene.subscribe(to: CollisionEvents.Began.self, componentType: GameMovementComponent.self, onCollisionBegan).store(in: &subscriptions)
    scene.subscribe(to: CollisionEvents.Updated.self,
                    componentType: CharacterMovementComponent.self,
                    onCollisionUpdated).store(in: &subscriptions)
    scene.subscribe(to: CollisionEvents.Ended.self, componentType: GameMovementComponent.self, onCollisionEnded).store(in: &subscriptions)
    }

    @MainActor
    func onCollisionBegan(event: CollisionEvents.Began) {
        let gameEntity = event.entityA
        let collisionEntity = event.entityB

        updateCollisionClassification(entityA: event.entityA, entityB: event.entityB, contacts: event.contacts)

        event.entityA.components[GameMovementComponent.self].currentlyTrackedCollisionEntity = event.entityB

        if let collisionClassification = event.entityA.components[GameMovementComponent.self].trackedCollisionEntities[event.entityB] {
            // If collision impulse reaches over a specific threshold, play a sound.
            if event.impulse > GameSettings.collisionImpulseThreshold {
                let audioEvent = AudioEventComponent(resourceName: "CollisionSound")
                gameEntity.components.set(audioEvent)
            }
        }
    }

    @MainActor
    func onCollisionUpdated(event: CollisionEvents.Updated) {
        updateCollisionClassification(entityA: event.entityA, entityB: event.entityB, contacts: event.contacts)
    }

    @MainActor
    func onCollisionEnded(event: CollisionEvents.Ended) {
        // Stop tracking.
        event.entityA.components[GameMovementComponent.self]?.trackedCollisionEntities[event.entityB] = nil

        if event.entityB == event.entityA.components[GameMovementComponent.self]?.currentlyTrackedCollisionEntity {
            event.entityA.components[GameMovementComponent.self]?.currentlyTrackedCollisionEntity = nil
    }


    private func updateCollisionClassification(entityA: Entity, entityB: Entity, contacts: [Contact]) {
        guard var collisionNormal = contacts.first?.normal else { return }

        // Normalize the collision normal.
        collisionNormal = normalize(collisionNormal)

        let collisionDot = dot(collisionNormal, [0, 1, 0])
        let classification: CollisionClassification = if collisionDot < -GameSettings.floorThreshold {
            .top 
        } else if collisionDot == GameSettings.floorThreshold {
            .floor(normal: collisionNormal)
        }  else {
           .inTheAir(normal: collisionNormal) 
        }

        entityA.components[GameMovementComponent.self].trackedCollisionEntities[entityB] = classification
    }
}
```

The collision sounds in Petite Asteroids are usually one-shot collision sounds, which the app plays using [`playAudio(_:)`](https://developer.apple.com/documentation/RealityKit/Entity/playAudio(_:)). For other collision sounds, the app groups a set of similar sounds together using an [`AudioFileGroupResource`](https://developer.apple.com/documentation/RealityKit/AudioFileGroupResource) to play nonrepeating random sounds for audio playback.

#### Design Dynamic Sounds

In this game, the Audio [`Entity`](https://developer.apple.com/documentation/RealityKit/Entity) uses an [`AmbientAudioComponent`](https://developer.apple.com/documentation/RealityKit/AmbientAudioComponent) for ambient audio. The system plays two audio files using [`AudioPlaybackController`](https://developer.apple.com/documentation/RealityKit/AudioPlaybackController) for the environment audio of the game. The character starts at the bottom of the butte with a calmer environment. As she rises up the butte, the calmer environment cross fades with the windier environment. The system blends these two files  according to how high the character ascends. In case she falls down, the windier environment fades gracefully by interpolating values over a number of seconds.

The sound stage design intentionally utilizes stereo music with spread and width (decorrelated content), so that any spatial sound effects in the game play closer to the center of the view. This way, the music doesn’t distract from the overall game experience, and improves the sense of immersion. To accomplish this effect, the app uses psychoacoustic and filtering techniques. So, at the bottom of the butte, the app uses a stereo recording asset, anchored to the volume. As you reposition the volume, the stereo recording follows it, so you can localize the app. The recording for the top of the butte has a quadraphonic (may be cube) surround layout, so as the character ascends the butte, the audio experience becomes increasingly immersive.

There’s an audio cue subsystem in Petite Asteroids’ audio system that controls playback of the app’s music. The sound effects of the game differ, depending on the scenes of the game. In the Fiery Descent sequence, the app plays back two layers simultaneously, with a mono layer playing as a spatial, high-frequency, single-channel point source and a stereo layer playing lower-frequency sounds with some subtle panning movement for immersion. One of the `fieryDescent` sounds, `fieryDescentSFXSpatial`, plays on `ParticleEmitter` entities for spatial audio that layers with ambient audio `fieryDescentSky` and `fieryDescentSFXAmbient`.

The design of the music scoring separates linear and nonlinear categories. The linear music at the end of the game triggers a cut scene and the app plays a linear music sequence. This scoring plays in sequence with the animation of the character, as the music doesn’t need to be interactive. The audio asset that plays for this instance is `outroMusic`. In terms of nonlinear music category, scores make the sound nonrepetitive. The sound design allows the app to cut the score into segments that it can loop infinitely and cleanly, while also allowing the audio to start playback at any randomized time. The `gameplayMusic`, `tutorialMusic`, and `menuMusic` all fall under this category.

###### Related Videos


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/enhancing-the-audio-experience-for-petite-asteroids)*