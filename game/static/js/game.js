document.addEventListener('DOMContentLoaded', function () {
    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            cell.textContent = cell.textContent === '' ? 'X' : 'O';
        });
    });
});
