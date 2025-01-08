document.addEventListener('DOMContentLoaded', function () {
    const playButton = document.getElementById('play-btn');
    const audioPlayer = document.getElementById('radioPlayer');
    const songInfo = document.getElementById('song-info');

    playButton.addEventListener('click', function () {
        audioPlayer.play();
        playButton.classList.add('d-none');
    });

    audioPlayer.addEventListener('play', function () {
        songInfo.textContent = "Reproduzindo: Dragão Negro - Jubarte Ataca";
    });
    audioPlayer.addEventListener('pause', function () {
        songInfo.textContent = "Pausado";
    });
});

