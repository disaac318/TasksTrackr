*TasksTrackr™*

(Developer: Dean Isaac)

**TaskTrackr™** TasksTrackr is a full-stack productivity platform developed for Milestone Project 3 to demonstrate robust, scalable, and secure data-centric web application development. Integrating Flask, MongoDB Atlas, and Bootstrap 5, the system delivers a seamless workflow for task creation, management, and prioritisation using a dynamic RAG status model based on due-date evaluation.

Authentication is implemented using secure password hashing, session management, and account freeze logic. Admins can oversee tasks/categories and freeze accounts, while superadmins add role changes, account deletion, and full-system visibility.
The UI is fully responsive and designed using Bootstrap 5, ensuring intuitive navigation and accessibility on all devices. The overall architecture supports modularity, maintainability, and multiple scalable pathways for future enhancements such as recurring tasks, calendar integration, and automated email or SMS reminders.

TasksTrackr exemplifies complete full-stack competency with secure backend operations, structured data modelling, administrative governance, and polished UX/UI implementation.

![Mockup image](assets/docs/wireframes/MockUp.png)

[Live webpage](https://tasks-tracker-77e68e91c21c.herokuapp.com)

## Table of Content

- [Game Logic Breakdown](#game-logic-breakdown)
    - [The game logic was developed using Javascript.](#the-game-logic-was-developed-using-javascript)
- [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Media](#media)
    - [Images](#images)
    - [Flaticon](#flaticon)
  - [Development Challenges and Resolutions](#development-challenges-and-resolutions)
    - [Problem 1: Favicon Icon Not Found](#problem-1-favicon-icon-not-found)
    - [Problem 2: Broken Player Hand Image Link (Whitespace Issue)](#problem-2-broken-player-hand-image-link-whitespace-issue)
    - [Problem 3: The car-front image is overlapping the game interface, causing visual obstruction during gameplay](#problem-3-the-car-front-image-is-overlapping-the-game-interface-causing-visual-obstruction-during-gameplay)
  - [What I Learned Along the Way](#what-i-learned-along-the-way)
    - [Working through this project was more than just completing a task—it was a meaningful personal learning journey that deepened my understanding of development best practices and significantly contributed to my growth as a developer. Throughout this process, I gained valuable insights, including:](#working-through-this-project-was-more-than-just-completing-a-taskit-was-a-meaningful-personal-learning-journey-that-deepened-my-understanding-of-development-best-practices-and-significantly-contributed-to-my-growth-as-a-developer-throughout-this-process-i-gained-valuable-insights-including)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### 🎯 User Goals

-  Play a simple, fun, and fast-paced game to relax or take a short mental break.
-  Challenge a computer opponent in a familiar game that requires quick thinking and strategy.
-  Enjoy a playful and visually engaging experience without needing to learn complex rules.
-  Compete against an AI with increasing difficulty to improve decision-making and prediction skills.
-  Enjoy the satisfaction of immediate visual and sound feedback with each win or round result.
-  Use the game as a light form of competition with friends or to simply pass time enjoyably.
-  Access a game that’s easy to play on any device — whether at home, during study breaks, or on the go.
-  Feel rewarded through engaging animations, effects, and theme customisation options.
-  Revisit the game multiple times thanks to its replayable nature and short, satisfying gameplay cycles.

### 🧑‍💼 Site Owner’s Goals

-  Design and develop a fully functional Rock-Paper-Scissors game that demonstrates strong command of JavaScript, HTML, CSS, and responsive design principles.
-  Showcase proficiency in front-end development by integrating animation, interactivity, and a polished user interface within a single-page application.
-  Apply modern development practices such as ES6 code structure, event-driven programming, and component reusability.
-  Implement visual feedback mechanisms (e.g., transitions, score animations, and win celebrations) to enhance user engagement.
-  Ensure the project reflects a high standard of accessibility, mobile responsiveness, and UI/UX design thinking.
-  Provide a smooth and enjoyable gameplay experience that encourages replayability and user retention.
-  Use this project as a portfolio piece to demonstrate technical capability, creativity, and a clear understanding of user-centered design.
-  Create clear and well-documented code that is easy to understand, extend, and maintain for future development or enhancement.

## 🎨 User Experience

The Rock-Paper-Scissors game is designed to provide an engaging and intuitive experience that balances simplicity with dynamic interactivity. Users are immediately drawn in by smooth animations, clear visual cues, and responsive controls that make gameplay enjoyable on any device. The interface supports quick decision-making through easily recognizable icons and provides immediate feedback via score updates, sound effects, and celebratory animations, fostering a rewarding sense of achievement. Overall, the experience is crafted to be accessible to users of all skill levels, encouraging repeat play through its polished design and seamless flow.

### 🎯 Target Audience

-  Casual gamers seeking a quick, entertaining distraction during breaks or downtime.
-  Beginners to gaming who appreciate simple, rule-light games with straightforward mechanics.
-  Students and professionals looking for a brief mental refresher or stress-relief tool.
-  Mobile users who want a fully responsive game playable across smartphones, tablets, and desktops.
-  Learners and hobbyist developers interested in frontend development concepts demonstrated through practical, interactive projects.
-  Anyone looking to enjoy a classic game with modern UI enhancements and AI challenge options.

### 📋 User Requirements and Expectations

-  **Easy and intuitive gameplay:** Users expect a straightforward interface where they can quickly understand how to play without prior instructions.
-  **Responsive design:** The game must work seamlessly across a range of devices, including smartphones, tablets, and desktops, adapting layout and controls accordingly.
-  **Clear feedback:** Users require immediate visual and auditory feedback after each move, including round outcomes, score updates, and celebratory effects when winning.
-  **Smooth transitions:** Animations such as card flips and gesture feedback should be fluid and not disrupt the flow of the game.
-  **Replayability:** Users expect to easily reset or start new games.
-  **Accessibility:** Controls and visuals must be clear, legible, and usable by players with varying abilities, including appropriate contrast and button sizes.
-  **Performance:** The game should load quickly and run smoothly without bugs or lag, ensuring a frustration-free experience.
-  **Privacy and security:** Users expect that the game runs entirely client-side, without collecting personal data or requiring internet connectivity.

### User Stories

#### What I need to know as a First-time User

1. I want to easily understand how to play Rock-Paper-Scissors without reading lengthy instructions, so I can start the game quickly.
2. I want clear, visually distinct buttons for Rock, Paper, and Scissors, so I can confidently make my choice.
3. I want real-time feedback showing which choice I made and what the computer chose, so I can follow the outcome clearly.
4. I want to see my current score and the computer’s score displayed prominently, so I can track the progress of the game.
5. I want the game to respond smoothly on my device (phone, tablet, or desktop), so I can play comfortably anywhere.
6. I want the option to reset or start a new game easily, so I can play multiple rounds without confusion.
7. I want simple sound and visual effects that enhance the experience without being distracting.

#### What I need to know as Returning Customer

1. I want to jump straight into the game without needing to relearn how it works, so I can enjoy quick, familiar gameplay.
2. I expect the interface to be consistent and responsive across devices, so I can continue playing on mobile, tablet, or desktop with ease.
3. I expect the game to load quickly and run smoothly, so I can immediately begin playing without interruptions.
4. I want visual and sound feedback to remain sharp and rewarding, maintaining the excitement of each round.
5. I want reliable performance with no bugs or crashes, so I can trust the experience every time I revisit.

## Testing User Stories from User Experience (UX) Section

### First Time User Experience

#### As a first-time user exploring the website, I want a clear and straightforward understanding of what the website offers, so I can decide quickly whether it matches my interest in fun, casual gameplay.

- The landing page includes a concise headline (e.g., "Choose your weapon and beat the Machine.") that clearly explains the site's purpose.
-  A short subheading or paragraph summarises the game (e.g., "Challenge the AI in this animated, responsive version of the classic game. No login needed.").
-  Prominent call-to-action (e.g., “Start Game” or “Flip to Play”) is visible without scrolling.
-  Flipcard animation or welcome message provides context before transitioning to gameplay.
-  The interface is intuitive, requiring no prior instructions to navigate.

#### As a first-time user exploring the website, I want to understand what to expect during my stay and seek information and confirmation that my investment will result in a satisfactory and enjoyable experience.

-  The website clearly communicates its purpose (e.g., "A fun and visually engaging Rock-Paper-Scissors game you can play anytime").
-  Visual elements (like animated cards or icons) indicate interactivity, fun, and ease of use.
-  Gameplay interface appears modern, polished, and inviting, with clear progression (e.g., animation, scoring).
-  Positive micro-interactions (sound effects, score feedback, gesture animations) enhance the sense of enjoyment.
-  No ads, distractions, or misleading links that could erode user trust.

## Design

### Design Choices

The Rock-Paper-Scissors (RPS) game was designed to offer an engaging, responsive, and visually appealing user experience while reflecting the classic simplicity and instant appeal of the original hand game. Key design considerations focused on intuitive interaction, game flow clarity, and playful aesthetics, ensuring both first-time and returning users can navigate and enjoy the platform with ease.

1. **Animated Flipcard Interface.** The landing page is structured as a single card that flips seamlessly into the game view. This introduces a minimalist one-page layout that reduces cognitive load and creates a dynamic transition between introduction and gameplay, reinforcing the immediacy of the experience.

2. **Mobile-First Responsive Design.** The interface is fully responsive across all screen sizes and devices. Whether accessed via desktop, tablet, or smartphone, the layout adapts proportionally to ensure that game buttons, scores, and animations remain accessible and visually balanced.
3. **Bold, Playful Aesthetics.** A lively color scheme—complemented by high-contrast light and dark themes—ensures strong visual clarity and aligns with the energetic nature of the game. These theme options also improve accessibility and personalisation.
4. **Intuitive Interaction and Feedback.** Visual icons for hand gestures (rock, paper, scissors) are supported by click animations and auditory feedback, creating a responsive environment that mimics real-world hand game interactions.
5. **Micro-Interactions and Transitions.** Subtle motion effects and transition animations (such as card flips, gesture reveals, and score changes) are used to enhance the perceived quality of the interface, without overwhelming the user or detracting from core functionality.
6. **No-Frills Navigation and Replayability.** Users are provided with clear calls-to-action (e.g., “ Game On ”, “Reset Game”) and minimal navigation barriers. Game sessions can be restarted instantly, promoting repeat engagement with a single click.
7. **Clean, Minimalist UI.** All visual elements are positioned to reduce clutter and emphasize gameplay. Icons, scores, instructions, and controls are arranged using a grid layout for balanced spatial alignment and simplicity.
8. **Performance Optimisation.** Images, animations, and JavaScript modules are optimised for quick loading and smooth transitions. Caching strategies and minimal asset bloat were prioritised to maintain seamless performance, even on slower networks.
9. **Distraction-Free Environment.** The site avoids intrusive elements such as advertisements or unnecessary popups.

### Colour Palette

![The Colour Palette](./assets/images/Colour-Palette.svg)
The overall color palette creates an inviting and user-friendly interface designed to enhance usability, emotional engagement, and thematic consistency.

**Vibrant Magenta/Purple (#990099 to #9069C range)**

-  Used in: Main headings, buttons (Rock, Paper, Scissors), and titles like “CHOOSE YOUR WEAPON”.
-  Psychology: Purple and magenta tones often evoke creativity, excitement, and boldness, which are ideal for a casual yet competitive game. It stands out against lighter backgrounds and draws user focus to the game’s core interactive elements.
-  UX Benefit: High contrast against the light background makes buttons and key text highly visible and accessible.

**Soft Lavender/Pastel Pink Background**

-  Used in: Background of the entire interface.
   Psychology: Light pastel tones provide a calming and non-intimidating atmosphere, which is essential for encouraging casual play and accessibility, especially for younger users or first-time players.
-  UX Benefit: This soft hue reduces eye strain while allowing stronger foreground colors (like purple or yellow) to pop effectively.

**Dark Green (#006400)**

-  Used in: Labels such as Player, Computer, and the Reset Game link.
-  Psychology: Green signifies fair play, progress, and positive action. It reinforces a sense of balance between the player and the computer and subtly invites users to reset and try again.
-  UX Benefit: Green is associated with success and restart in digital interfaces, making it intuitive for the user.

**Golden Yellow (#FFC107)**

-  Used in: The score count for both Player and Computer.
   Psychology: Yellow evokes energy, attention, and alertness, ideal for highlighting dynamic elements like scores.
-  UX Benefit: Easily catches the user's eye and signifies real-time change, keeping users informed about game status.

**Dark Tyrian Purple (#330033)**

-  Used in: Footer text for legal and branding content.
-  Reasoning: This subtle but readable contrast anchors the footer information without competing with the main content.

### Fonts

**Acme (Headlines & Buttons) — Adds Playfulness**

-  Game-like personality: Acme's rounded, bold letterforms convey a fun, casual, and energetic tone—perfect for a game targeting users of all ages, especially younger audiences or casual players.
-  Attention-grabbing: Ideal for use in titles like “Rock! Paper! Scissors!”and scoreboard headings. 
-  Web-optimized: Loads fast from Google Fonts and maintains quality on all screen sizes.

**Helvetica (Body, Instructions, UI) — Ensures Clarity**

-  Clean and timeless: Helvetica’s neutral design ensures the interface stays readable, even during fast-paced interactions.
-  Widely supported: Helvetica is a system font on many devices, which improves performance and reduces font flickering.
-  Professional balance: While Acme plays up the fun, Helvetica brings the visual balance and polish your site needs to appear well-structured.

### Wireframes

<details><summary>Desktop</summary>
<img src="./assets/docs/wireframes/wireFrame RPS desktop.svg">
</details>
<details><summary>Tablet</summary>
<img src="./assets/docs/wireframes/wireFrame RPS tablet.svg">
</details>
<details><summary>Phone</summary>
<img src="./assets/docs/wireframes/wireFrame RPS phone.svg">
</details>

## Technologies Used

### Languages

-  HTML
-  CSS
-  Javascript
-  Bootstrap 5.0

### Frameworks & Tools

-  Bootstrap v5.0
-  Git
-  GitHub
-  adobe Illustrator
-  Google Fonts

## Features

A single-page layout is used, with a flip effect that transitions into the main game environment.

### 🃏 Landing Card (Welcome Interface)

![The Landing Card](./assets/images/RPS-FlipCard1.png)

The application opens with a visually engaging landing card, designed to welcome the player and introduce the Rock-Paper-Scissors game. This card serves as the entry point to the gameplay experience and includes:

-  A brief title and subtitle to establish the game’s theme.
-  A “Start Game” button that triggers a smooth flip animation, transitioning the interface into the main game screen.
-  Responsive and styled using Bootstrap and CSS.
-  Purposefully minimalist to maintain focus and provide a clean first impression.

The transition from this card to the game interface is seamless, enhancing user engagement through an animated card-flip effect that simulates a dynamic and interactive experience—all while keeping the app as a single-page application (SPA).

### 🎮 Flip Card 2 (Main Game Interface)

![The Landing Card](./assets/images/RPS-FlipCard2.png)

Upon initiating the game, the landing card flips to reveal Flip Card 2, the core gameplay interface. This card presents an intuitive, animated layout where users actively engage in the Rock-Paper-Scissors challenge. Key elements include:

-  Animated hand gesture icons for Rock 🪨, Paper 📄, and Scissors ✂️, allowing players to make a selection
-  A real-time scoreboard that tracks player and computer scores across rounds
-  AI opponent logic, with adjustable difficulty (if implemented).
-  Responsive layout using Bootstrap for smooth performance across devices
-  Optional sound effects and celebration animations (e.g., confetti or audio) when a player wins a match.

All interactions remain within this single view, preserving the single-page application architecture. This card is where the game logic, UI transitions, and feedback mechanisms converge to deliver an engaging user experience.

### 🔬 Suggestions for Future Enhancements

-  **Difficulty Mode:** Use weighted randomness for computer choices.
-  **Match History Log:** Store rounds and render to UI.
-  **Theming:** Toggle dark/light styles.
-  **Accessibility Improvements:** Add ARIA labels, focus states, and keyboard navigation.

## Validation

### HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website. All pages pass with no errors no warnings to show.

<details><summary>HTML</summary>
<img src="./assets/docs/validation/html-validation.png">
</details>

### CSS Validation

<details><summary>style.css</summary>
<img src="./assets/docs/validation/css-validation.png">
</details>

### Performance

Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website.

<details><summary>Flip Card 1</summary>
<img src="./assets/docs/validation/LH-Validation.png">
</details>

### JS Lint

**Code Quality and Validation.**

<img src="./assets/docs/validation/before-JSLint.png">

To ensure the JavaScript code adheres to best practices and is free of common errors, I installed the JSLint extension for Visual Studio Code. This tool automatically analyzes the script and displays any warnings or errors in the editor’s right panel. I systematically reviewed each reported issue and applied the necessary fixes to improve code quality.

JSLint reported 18 warnings and errors that required correction. I carefully reviewed each issue and made the necessary code adjustments to ensure compliance with JavaScript best practices and improve overall code quality.
This iterative process was repeated until the code passed JSLint validation without any errors or warnings, ensuring a clean and maintainable codebase.

<img src="./assets/docs/validation/JSLint-compliant.png">

Here, although JSLint flagged the semicolon as an error, it is syntactically necessary to correctly terminate the function expression and prevent potential parsing issues.

# Game Logic Breakdown

<img src="./assets/images/RPS-FlowChart.svg">

### The game logic was developed using Javascript.

1. **Event-Driven Start**

-  **DOMContentLoaded** ensures that the script runs only after the HTML is fully loaded.

2. **Intro Transition**

-  Clicking the Flip Button: (Game On)
-  Adds **.flipped class** to reveal the match screen.
-  Plays a “woosh” transition sound.

3. **Game Initialization**-
   **Function game()** encapsulates all logic and is executed immediately.

-  Initializes:
-  Scores
-  Audio elements
-  DOM references
-  Game state **(isGameOver)**

4. **User Interaction Loop**

-  **Player clicks a weapon (rock/paper/scissors):**
-  The computer generates a random move.
-  Both hand images animate.
-  After 2 seconds, the hands update and **decideWinner()** is called.

5. **Winner Decision Logic**

-  If same choice: draw
-  If player wins: increment player score
-  If computer wins: increment computer score
-  Update the visual scoreboard with animation

6. **Game End Condition**

-  **If player or computer reaches 3 points:**
-  Game is marked over **(isGameOver = true)**
-  Shows victory/defeat message
-  Triggers celebration (confetti) or defeat rain (dark confetti)
-  Plays special sound

7. **Game Reset**

-  The Reset button calls **resetGame():**
-  Resets all scores and visual states
-  Restores initial hand positions
-  Allows replay

The RPS game logic exemplifies a well-structured, modular, event-driven, and state-based design approach. Key functionalities are encapsulated within modular functions such as **updateScoreboard, decideWinner, celebrate**, and **resetGame**, which enhances code maintainability, readability, and ease of testing. The use of animations and audio feedback significantly improves user engagement, making the gameplay experience more interactive and visually appealing. Additionally, the implementation of a game state variable **(isGameOver)** ensures input is effectively disabled once a match concludes, preventing unintended actions and maintaining logical integrity throughout the game flow.

# Performing tests on various devices

The website was tested on the following devices:

-  Imac 24-inch M1 2021
-  Ipad Pro 11 2021
-  Apple Iphone 14 Pro

In addition, the website was tested using Google Chrome Developer Tools Device Toggeling option for all available device options.

### Browser compatibility

The website was tested on the following browsers:

-  Safari
-  Google Chrome
-  Mozilla Firefox
-  Microsoft Edge

## Deployment

The website was deployed using GitHub Pages by following these steps:

1. In the GitHub repository navigate to the Settings tab
2. On the left hand menu select Pages
3. For the source select Branch: master
4. After the webpage refreshes automaticaly you will see a ribbon on the top saying: " Your site is live at https://disaac318.github.io/Rock-Paper-Scissors-The-Frontend-Challenge/ "

## Credits

### Media

All sound effects used in this project were sourced from <a href="https://pixabay.com/sound-effects/">Pixabay</a>, a platform offering high-quality, royalty-free media. I am grateful to the generous creators who share their work freely for public use.

### Images

The visual assets and game illustrations were designed and created by me using Adobe Illustrator. This allowed for a fully customised interface and ensured a cohesive aesthetic that aligns with the interactive and playful nature of the game.

### Flaticon

The favicon used in this project was sourced from <a href="https://www.flaticon.com">Flaticon</a>, a reputable resource for high-quality vector icons. I then converted the image to .ico format using an online converter to ensure compatibility across browsers, and placed it in the root directory as favicon.ico.

## Development Challenges and Resolutions

### Problem 1: Favicon Icon Not Found

<details><summary><strong>Favicon Icon Not Found</strong></summary>
<img src="./assets/images/Screenshot 2025-06-26 at 05.39.28.png">
</details>

**Issue:**  
The browser attempted to load the favicon (`favicon.ico`) from the default location, but the file was missing. When running the site locally (e.g., via Live Server or localhost), the browser requests:  
`http://127.0.0.1:5502/favicon.ico`  
If the favicon file is absent in the project root, this results in a `404 (Not Found)` error.

**How I fixed it:**  
<img src="./favicon.ico">

1. Added a `favicon.ico` file to the root directory of the project.
2. Linked the favicon explicitly in the HTML `<head>` section:

<link rel="icon" href="/favicon.ico" type="image/x-icon">

### Problem 2: Broken Player Hand Image Link (Whitespace Issue)

<details><summary><strong>Broken image link</strong></summary>
<img src="./assets/images/Screenshot 2025-06-26 at 05.36.40.png">
</details>

**Issue:**
The game failed to display the player hand image because the constructed image file path contained extraneous whitespace, leading to an invalid URL and a 404 (Not Found) error. For example:
GET http://127.0.0.1:5502/assets/images/ rock .svg 404 (Not Found)

This happened because the player’s choice was extracted from the button text without trimming whitespace:

const playerChoice = button.textContent.toLowerCase();

If the button’s label contained spaces (e.g., <button> Rock </button>), the resulting string was " rock " instead of "rock".

**How I fixed it:**
I used .trim() to sanitize the input and remove unwanted whitespace:

const playerChoice = button.textContent.trim().toLowerCase();
This ensured the file path was correctly formed, for example:
./assets/images/rock.svg

### Problem 3: The car-front image is overlapping the game interface, causing visual obstruction during gameplay

<details><summary><strong>Front Card Image Overlapping Game Interface</strong></summary>
<img src="./assets/images/image-overlap.png">
</details>

**Issue:**
When deployed on GitHub Pages, the front card remained visible and overlapped the back card during the flip animation, causing a UI glitch.

**How I fixed it:**

Adjusted CSS to properly manage the visibility and layering of card faces during state transitions:

<details><summary><strong>CSS Correction</strong></summary>
<img src="./assets/images/css-correction.png">
</details>

<details><summary><strong>Result Image</strong></summary>
<img src="./assets/images/card-front-noShow.png">
</details>

## What I Learned Along the Way

### Working through this project was more than just completing a task—it was a meaningful personal learning journey that deepened my understanding of development best practices and significantly contributed to my growth as a developer. Throughout this process, I gained valuable insights, including:

-  **Meticulous Asset Management:**
   Ensuring all static resources like favicons are correctly linked and available prevents avoidable runtime errors and improves the professionalism of the application. <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#attr-rel">MDN Web Docs - favicon</a>
-  **Data Sanitization and Defensive Coding:**
   Sanitizing dynamic inputs before use—such as trimming whitespace—is essential to avoid subtle bugs, especially when those inputs determine critical file paths or UI behavior. <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim">JavaScript String.prototype.trim() - MDN</a>
-  **Mastering CSS for UI State Control:**
   A deep understanding of CSS properties such as z-index, opacity, and pointer-events is crucial to managing UI element visibility and interactivity, particularly in animations and transitions. <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/z-index">CSS z-index - MDN</a>
-  **Cross-Environment Testing:**
   Issues can arise uniquely in different deployment environments. Testing on platforms like GitHub Pages helped identify and fix problems that did not surface in local development. <a href="https://docs.github.com/en/pages">GitHub Pages Documentation</a>
-  **Systematic Debugging Process:**
   Approaching errors methodically—isolating causes, applying targeted fixes, and iterating—improves not only the final product but also one’s troubleshooting skills and code maintainability.
-  **Enhancing User Experience Through Visual Polish:**
   Correct rendering and smooth transitions are vital for user engagement and convey a sense of quality and attention to detail in the application.

Together, these insights have strengthened my practical skills in frontend development and equipped me to anticipate and resolve similar challenges efficiently in future projects.

## Acknowledgements

This project was developed as part of my learning journey in Diploma in Web Application Development (DIWAD), with significant inspiration drawn from The Odin Project. I extend my sincere thanks to the creators and contributors of The Odin Project for their well-structured curriculum and community-driven resources, which served as a guiding framework throughout this build.

I am also grateful to my mentor for his support and constructive feedback, and to the broader developer community—including Stack Overflow, GitHub, and MDN Web Docs—for the wealth of knowledge and collaborative spirit they provide.

This Rock-Paper-Scissors game reflects both my growing understanding of JavaScript fundamentals and my commitment to writing clean and testable code.
