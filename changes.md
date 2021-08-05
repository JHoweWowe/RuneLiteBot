# Version Changes:

## Version 1.0 Features:
- [x] Improve findRandomTree() algorithm where bot may accidently mistake a log for a tree
    - Implemented confirmTree() algorithm
    - Pixel color detection for finding tree outside of inventory - this approach speeds up algorithm slightly 
- [x] Create Python script for additional support
- [x] Create time variable if user isn't able to detect tree within max number of attempts

## Version 1.1 Features:
- [x] Implement basic configuration file
    - Prevents end-user from having to key in settings repeatedly
- [x] Create first rough draft of the OSRSBot UI
    - Reads existing configuration file
    - Implement both START button 
    - Doesn't fully function due to lack of asynchronous programming
- [x] Add supporting images and videos for better understanding of documentation
- [x] Refactored code for Main execution script for OOP principles

## TODO Additional Features:
- [ ] Make dropLogs() algorithm more advanced (if needed)
- [ ] Include Youtube demo video
- [ ] Create another findTree() algorithm where color detection starts from center of window??
- [ ] OSRS main client support?
- [ ] Support Window Scaling

## TODO Features for Version 2:
- [ ] Implement OpenCV
- [ ] TensorFlow machine learning algorithm
- [ ] Improve Usability
    - [ ] Enhance UI
    - [ ] Create an executable Windows exe file?
    - [ ] Integrate GUI together with concurrency support
