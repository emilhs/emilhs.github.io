<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Provincial Team Qualification Calculator</title>
</head>
<body>

<h1>Provincial Team Qualification Calculator</h1>

<p>
Select the athlete's two best performances and enter the times in seconds.
(Placeholder standards: 500m = 60 s, 1000m = 120 s, 1500m = 180 s)
</p>

<h2>Performance 1</h2>

<label>Event:</label>
<select id="event1">
    <option value="60">500m (Standard: 60 s)</option>
    <option value="120">1000m (Standard: 120 s)</option>
    <option value="180">1500m (Standard: 180 s)</option>
</select>

<label>Time (seconds):</label>
<input type="number" id="time1" step="0.001">

<h2>Performance 2</h2>

<label>Event:</label>
<select id="event2">
    <option value="60">500m (Standard: 60 s)</option>
    <option value="120">1000m (Standard: 120 s)</option>
    <option value="180">1500m (Standard: 180 s)</option>
</select>

<label>Time (seconds):</label>
<input type="number" id="time2" step="0.001">

<br><br>

<button onclick="calculate()">Calculate Qualification</button>

<hr>

<div id="results"></div>

<hr>

<h2>Example from Policy</h2>

<p>
Skater A has:
</p>

<ul>
<li>500m = 43.707 s</li>
<li>1500m = 2:15.964 (135.964 s)</li>
<li>500m Standard = 39.660 s</li>
<li>1500m Standard = 2:06.565 (126.565 s)</li>
</ul>

<p>
500m Percentage = 43.707 ÷ 39.660 × 100 = 110.192%
</p>

<p>
1500m Percentage = 135.964 ÷ 126.565 × 100 = 107.426%
</p>

<p>
Cumulative Average = (110.192 + 107.426) ÷ 2 = 108.809%
</p>

<p>
Result: Team Level A3
</p>

<button onclick="runExample()">Run Example</button>

<div id="exampleResult"></div>

<script>

function determineLevel(percent) {

    if (percent <= 106) {
        return "A1";
    }

    if (percent <= 108) {
        return "A2";
    }

    if (percent <= 110) {
        return "A3";
    }

    if (percent <= 112) {
        return "B1";
    }

    if (percent <= 115) {
        return "B2 / Dev T";
    }

    return "Not Qualified";
}

function calculate() {

    const athlete1 = parseFloat(document.getElementById("time1").value);
    const athlete2 = parseFloat(document.getElementById("time2").value);

    const standard1 = parseFloat(document.getElementById("event1").value);
    const standard2 = parseFloat(document.getElementById("event2").value);

    if (isNaN(athlete1) || isNaN(athlete2)) {

        document.getElementById("results").innerHTML =
            "<p>Please enter both race times.</p>";

        return;
    }

    const percent1 = (athlete1 / standard1) * 100;
    const percent2 = (athlete2 / standard2) * 100;

    const cumulativePercent = (percent1 + percent2) / 2;

    const level = determineLevel(cumulativePercent);

    document.getElementById("results").innerHTML = `
        <h2>Results</h2>

        <p><strong>Performance 1 Percentage:</strong>
        ${percent1.toFixed(3)}%</p>

        <p><strong>Performance 2 Percentage:</strong>
        ${percent2.toFixed(3)}%</p>

        <p><strong>Cumulative Average Percentage:</strong>
        ${cumulativePercent.toFixed(3)}%</p>

        <p><strong>Team Level:</strong>
        ${level}</p>

        <h3>Calculation</h3>

        <p>
        (${percent1.toFixed(3)} + ${percent2.toFixed(3)}) ÷ 2
        = ${cumulativePercent.toFixed(3)}%
        </p>
    `;
}

function runExample() {

    const athlete500 = 43.707;
    const athlete1500 = 135.964;

    const standard500 = 39.660;
    const standard1500 = 126.565;

    const percent500 = (athlete500 / standard500) * 100;
    const percent1500 = (athlete1500 / standard1500) * 100;

    const average = (percent500 + percent1500) / 2;

    const level = determineLevel(average);

    document.getElementById("exampleResult").innerHTML = `
        <hr>

        <h3>Example Calculation</h3>

        <p>500m Percentage:
        ${percent500.toFixed(3)}%</p>

        <p>1500m Percentage:
        ${percent1500.toFixed(3)}%</p>

        <p>Cumulative Average:
        ${average.toFixed(3)}%</p>

        <p><strong>Result:
        ${level}</strong></p>
    `;
}

</script>

</body>
</html>