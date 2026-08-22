function App() {
  return (
    <main className="shell">
      <section className="hero">
        <p className="eyebrow">Employee Shuttle Reliability Platform</p>
        <h1>Reliable transport, without continuous tracking.</h1>
        <p className="subtitle">
          Privacy-first shuttle scheduling, event-based pickup verification,
          alerts, and operational insights.
        </p>
        <div className="cards">
          <article><span>01</span><h2>Scheduled</h2><p>Trips are driven by configured schedules and routes.</p></article>
          <article><span>02</span><h2>Verified</h2><p>Location is checked only when a driver records a key event.</p></article>
          <article><span>03</span><h2>Observable</h2><p>HR gets reliable trip history and exception signals.</p></article>
        </div>
      </section>
    </main>
  );
}
export default App;
