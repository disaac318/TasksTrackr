// Basic flash-message animation: blink a few times, then auto-dismiss.
document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll(".flash-alert");

    alerts.forEach(alert => {
        const duration = parseInt(alert.getAttribute('data-effect-duration')) || 5000;

        // Blink 3 times over the duration
        let blinkCount = 0;
        const blinkInterval = setInterval(() => {
            alert.classList.toggle("blink");  // toggle opacity
            blinkCount++;

            if (blinkCount >= 6) { // 3 blinks = 6 toggles
                clearInterval(blinkInterval);
                alert.classList.remove("blink");
                
                // Fade out using Bootstrap 5's dismiss
                const closeBtn = alert.querySelector('.btn-close');
                if (closeBtn) {
                    setTimeout(() => closeBtn.click(), 250); // small delay for smooth fade
                }
            }
        }, duration / 6); // spread 3 blinks over total duration
    });
});
