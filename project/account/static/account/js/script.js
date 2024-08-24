!function() {
    const message = document.querySelector('.message');
    if (message == null) return;

    let removed = false;
    const inputs = document.querySelectorAll('.input-target');

    for (const input of inputs) {
        input.addEventListener('keydown', () => {
            if (removed) return;

            removed = true;
            message.remove();
        });
    }
}();
