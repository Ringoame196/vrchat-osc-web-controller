// 直進
function startAction() {
    document.getElementById("status").innerText = "直進中...";
    fetch('/start', { method: 'POST' });
}

// ダッシュ
function startDash() {
    document.getElementById("status").innerText = "ダッシュ中...";
    fetch('/dash', { method: 'POST' });
}

// 後退
function startBack() {
    document.getElementById("status").innerText = "後退中...";
    fetch('/back', { method: 'POST' });
}

// 停止（どちらのボタンを離しても止まる）
function stopAction() {
    document.getElementById("status").innerText = "停止中";
    fetch('/stop', { method: 'POST' });
}