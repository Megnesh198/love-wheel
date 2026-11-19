const LOVE_100 = [
  "I love you", "Tum meri duniya ho", "I adore you", "Dil se chahta hoon tumhe",
  "You mean everything to me", "Meri har khushi tumse hai", "I'm crazy about you", "Tum mere dil ki dhadkan ho",
  "You have my heart", "Har pal tumhari yaad aati hai", "I love you endlessly", "Tum ho toh sab kuch hai",
  "You are my world", "Meri subah aur shaam tum ho", "I'm deeply in love with you", "Tumse mil kar zindagi badal gayi",
  "You complete me", "Tum meri sabse pyari aadat ho", "I love you more each day", "Meri har dua mein tum ho",
  "You're my favorite person", "Tumhari muskaan sabse anmol hai", "I cherish you", "Dil bas tumhe hi maangta hai",
  "My heart belongs to you", "Tum meri jaan ho", "I love you to the moon", "Har lamha tumhare saath jeena hai",
  "You're my everything", "Tumse behtar kuch nahi", "I'm madly in love with you", "Meri duniya tum par rukti hai",
  "I treasure every moment with you", "Tum meri roshni ho", "You light up my life", "Dil ke sabse kareeb tum ho",
  "I love you unconditionally", "Har baat mein tumhara zikr hota hai", "You are my home", "Tumhare bina adhoora hoon",
  "I can't get enough of you", "Tum meri sabse badi taqat ho", "You're my sunshine", "Meri har khwahish tum ho",
  "I love you beyond words", "Tumhari aankhon mein apni duniya dekhi", "My heart skips a beat for you", "Har din tumpe naya pyaar aata hai",
  "You're the best part of my day", "Tum ho toh dar kaisa", "I'm so lucky to have you", "Mera dil sirf tumhara hai",
  "I love you forever and always", "Tum meri kismat ka sabse haseen hissa ho", "You're my soulmate", "Har saans tumhare naam",
  "I fall for you every single day", "Tumhari baatein dil ko chhoo jaati hain", "You're my greatest blessing", "Mera har sapna tumse shuru hota hai",
  "I love you with all my heart", "Tum meri pehli aur aakhiri pasand ho", "You're my safe place", "Dil ko sukoon sirf tumse milta hai",
  "I'm hopelessly in love with you", "Tum meri zindagi ki sabse khoobsurat kahani ho", "You make life magical", "Har pal tumhe aur chahta hoon",
  "I love you purely", "Tum meri har muskaan ki wajah ho", "You're my dream come true", "Meri har khushi ka raaz tum ho",
  "I'm drawn to you endlessly", "Tumse juda hona namumkin hai", "You're my guiding star", "Andheron mein mera sahara tum ho",
  "I love you fiercely", "Dil ne bas tumhe chuna hai", "My soul recognizes yours", "Humara rishta sabse khaas hai",
  "You're my sweetest obsession", "Har waqt bas tumhara khayal rehta hai", "I love you through every season", "Dhoop ho ya chhaon, main tumhare saath hoon",
  "You're my heart's desire", "Meri har chahat tum par khatam hoti hai", "I'm devoted to you", "Tumhare liye sab kuch qubool hai",
  "You bring peace to my soul", "Tumhari aawaz se dil shaant ho jaata hai", "I love you more than yesterday", "Aaj kal se zyada pyaar karta hoon",
  "You're my forever person", "Har janam mein tumhe hi chahunga", "I admire everything about you", "Tumhara har andaaz pyara lagta hai",
  "You're the reason I smile", "Tumhari ek hansi kaafi hai", "I love you without limits", "Pyaar ki koi seema nahi",
  "My world revolves around you", "Meri duniya ka markaz tum ho", "You're my true north", "Bhatakne par rasta dikhane waale tum ho",
  "I'm fond of every little thing about you", "Tumhari chhoti-chhoti baatein bhi yaad rehti hain", "You're my heart's melody", "Dil ka geet tum ho",
  "I love you completely", "Poora ka poora dil tumhara hai", "You're my favorite place to be", "Tumhare paas rehna sabse achha lagta hai",
  "I'm enchanted by you", "Tumhara jaadoo dil par chha gaya hai", "You're my eternal love", "Hamesha rehne waala pyaar",
  "I love you softly and deeply", "Gehraiyon se nikla hua pyaar", "You're my comfort and joy", "Mera chain aur meri khushi tum ho",
  "I'm wrapped around your heart", "Dil tumhare haathon mein mehfooz hai", "You're my one and only", "Tum jaisa koi aur nahi",
  "I love you in every universe", "Har duniya mein sirf tumhara", "You're my quiet happiness", "Khamoshi mein bhi tumhara saath",
  "I'm captivated by your spirit", "Tumhari zindadili sabse alag hai", "You're my precious gem", "Mera sabse keemti heera tum ho",
  "I love you faithfully", "Wafa ka doosra naam tum ho", "You're my warm embrace", "Tumhari baahon mein sukoon hai",
  "I'm thrilled to call you mine", "Tumhe apna kehna sabse bada garv hai", "You're my constant inspiration", "Aage badhne ki prerana tum ho",
  "I love you generously", "Bina kisi shart ke pyaar", "You're my sweetest memory", "Sabse meethi yaad tum ho",
  "I love you. Always.", "Main tumse pyaar karta hoon. Hamesha."
].slice(0, 100);

const THEMES = [
  {
    bg: [22, 6, 20],
    ringOuter: [244, 162, 97],
    ringInner: [255, 77, 141],
    c1: [255, 110, 165],
    c2: [255, 205, 130],
    c3: [245, 155, 225],
    centerFill: [34, 9, 30],
    textMain: [255, 245, 248],
  },
  {
    bg: [12, 8, 28],
    ringOuter: [255, 125, 200],
    ringInner: [165, 130, 255],
    c1: [255, 130, 210],
    c2: [185, 145, 255],
    c3: [255, 195, 235],
    centerFill: [22, 13, 44],
    textMain: [252, 245, 255],
  },
  {
    bg: [25, 8, 12],
    ringOuter: [255, 140, 90],
    ringInner: [255, 95, 115],
    c1: [255, 105, 120],
    c2: [255, 175, 105],
    c3: [255, 215, 150],
    centerFill: [40, 12, 18],
    textMain: [255, 248, 242],
  },
  {
    bg: [16, 5, 26],
    ringOuter: [225, 120, 255],
    ringInner: [255, 80, 165],
    c1: [215, 110, 255],
    c2: [255, 90, 175],
    c3: [255, 180, 230],
    centerFill: [28, 8, 42],
    textMain: [255, 244, 255],
  },
];

const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const cleanBtn = document.getElementById("cleanBtn");

const cx = canvas.width / 2;
const cy = canvas.height / 2;

let cleanMode = false;
function setCleanMode(state) {
  cleanMode = state;
  cleanBtn.style.display = cleanMode ? "none" : "block";
}
cleanBtn.addEventListener("click", () => setCleanMode(true));
window.addEventListener("keydown", (e) => {
  if (e.key.toLowerCase() === "c") setCleanMode(!cleanMode);
  else if (e.key === "Escape" && cleanMode) setCleanMode(false);
});

const lerp = (a, b, t) => a + (b - a) * t;
const lerpRgb = (a, b, t) => [
  Math.round(lerp(a[0], b[0], t)),
  Math.round(lerp(a[1], b[1], t)),
  Math.round(lerp(a[2], b[2], t)),
];
const toRgb = (rgb) => `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

function getPalette(progress) {
  const n = THEMES.length;
  const iA = Math.floor(progress) % n;
  const iB = (iA + 1) % n;
  const rawT = progress - Math.floor(progress);
  const t = rawT * rawT * (3 - 2 * rawT);
  const a = THEMES[iA], b = THEMES[iB];
  return {
    bg: lerpRgb(a.bg, b.bg, t),
    ringOuter: lerpRgb(a.ringOuter, b.ringOuter, t),
    ringInner: lerpRgb(a.ringInner, b.ringInner, t),
    c1: lerpRgb(a.c1, b.c1, t),
    c2: lerpRgb(a.c2, b.c2, t),
    c3: lerpRgb(a.c3, b.c3, t),
    centerFill: lerpRgb(a.centerFill, b.centerFill, t),
    textMain: lerpRgb(a.textMain, b.textMain, t),
  };
}

function getGradientColor(idx, total, pal) {
  const ratio = idx / Math.max(1, total);
  if (ratio < 0.5) return toRgb(lerpRgb(pal.c1, pal.c2, ratio * 2));
  return toRgb(lerpRgb(pal.c2, pal.c3, (ratio - 0.5) * 2));
}

function drawMiniHeart(x, y, size, color) {
  ctx.save();
  ctx.translate(x, y);
  ctx.beginPath();
  for (let deg = 0; deg <= 360; deg += 15) {
    const rad = (deg * Math.PI) / 180;
    const hx = 16 * Math.pow(Math.sin(rad), 3);
    const hy = -(13 * Math.cos(rad) - 5 * Math.cos(2 * rad) - 2 * Math.cos(3 * rad) - Math.cos(4 * rad));
    const px = (hx / 16) * size;
    const py = (hy / 16) * size;
    if (deg === 0) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  }
  ctx.closePath();
  ctx.fillStyle = color;
  ctx.fill();
  ctx.restore();
}

const stars = Array.from({ length: 125 }, () => ({
  x: 15 + Math.random() * (canvas.width - 30),
  y: 15 + Math.random() * (canvas.height - 30),
  r: 0.7 + Math.random() * 2.1,
  phase: Math.random() * Math.PI * 2,
}));

let angleOffset = 0;
let orbitAngle = 0;
let themeProgress = 0;
let visibleCount = 0;
let frame = 0;

let spotlightIdx = 0;
let spotlightTimer = 0;
let targetCenterMsg = "";
let typedChars = 0;
let typeTick = 0;

function wrapText(text, maxWidth) {
  const words = text.split(" ");
  const lines = [];
  let current = "";
  for (const word of words) {
    const test = current ? `${current} ${word}` : word;
    if (ctx.measureText(test).width <= maxWidth) {
      current = test;
    } else {
      if (current) lines.push(current);
      current = word;
    }
  }
  if (current) lines.push(current);
  return lines;
}

function animate() {
  const pal = getPalette(themeProgress);
  const bgCss = toRgb(pal.bg);
  document.body.style.background = bgCss;

  ctx.fillStyle = bgCss;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const starCol = toRgb(pal.c3);
  for (const s of stars) {
    const tw = (Math.sin(frame * 0.07 + s.phase) + 1) / 2;
    const rad = s.r * (0.65 + 0.55 * tw);
    ctx.beginPath();
    ctx.arc(s.x, s.y, rad, 0, Math.PI * 2);
    ctx.fillStyle = starCol;
    ctx.fill();
  }

  const orbitR = 382;
  const outerCol = toRgb(pal.ringOuter);
  for (let deg = 0; deg < 360; deg += 8) {
    const rad = ((deg + orbitAngle * 0.65) * Math.PI) / 180;
    const dx = cx + orbitR * Math.cos(rad);
    const dy = cy + orbitR * Math.sin(rad);
    ctx.beginPath();
    ctx.arc(dx, dy, 1.5, 0, Math.PI * 2);
    ctx.fillStyle = outerCol;
    ctx.fill();
  }

  const numHearts = 8;
  for (let hIdx = 0; hIdx < numHearts; hIdx++) {
    const hDeg = (360 / numHearts) * hIdx - orbitAngle * 1.15;
    const hRad = (hDeg * Math.PI) / 180;
    const hx = cx + orbitR * Math.cos(hRad);
    const hy = cy + orbitR * Math.sin(hRad);
    const pulseSize = 6.5 + 1.8 * Math.sin(frame * 0.1 + hIdx);
    drawMiniHeart(hx, hy, pulseSize, getGradientColor(hIdx, numHearts, pal));
  }

  if (visibleCount < LOVE_100.length && frame % 2 === 0) {
    visibleCount++;
  }

  if (visibleCount > 0) {
    spotlightTimer++;
    if (spotlightTimer >= 105) {
      spotlightTimer = 0;
      spotlightIdx = (spotlightIdx + 1) % visibleCount;
    }
    const desired = LOVE_100[spotlightIdx];
    if (desired !== targetCenterMsg) {
      targetCenterMsg = desired;
      typedChars = 0;
      typeTick = 0;
    }
    if (typedChars < targetCenterMsg.length) {
      typeTick++;
      if (typeTick % 2 === 0) typedChars++;
    }
  }

  const outerR = 342;
  const innerR = 124;
  ctx.beginPath();
  ctx.arc(cx, cy, outerR, 0, Math.PI * 2);
  ctx.strokeStyle = outerCol;
  ctx.lineWidth = 1.6;
  ctx.stroke();

  ctx.beginPath();
  ctx.arc(cx, cy, innerR, 0, Math.PI * 2);
  ctx.strokeStyle = toRgb(pal.ringInner);
  ctx.lineWidth = 1.4;
  ctx.stroke();

  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  for (let i = 0; i < visibleCount; i++) {
    const deg = (360 / LOVE_100.length) * i + angleOffset;
    const rad = (deg * Math.PI) / 180;
    const wave = Math.sin(frame * 0.06 + i * 0.28) * 11;
    const isSpot = i === spotlightIdx;
    const textR = 236 + wave + (isSpot ? 7 : 0);

    const tx = cx + textR * Math.cos(rad);
    const ty = cy + textR * Math.sin(rad);

    let dispDeg = (-deg) % 360;
    if (dispDeg < 0) dispDeg += 360;
    if (dispDeg > 90 && dispDeg < 270) {
      dispDeg = (dispDeg + 180) % 360;
    }

    ctx.save();
    ctx.translate(tx, ty);
    ctx.rotate((-dispDeg * Math.PI) / 180);
    ctx.font = isSpot ? "bold 11px Consolas, monospace" : "10px Consolas, monospace";
    ctx.fillStyle = isSpot ? toRgb(pal.textMain) : getGradientColor(i, LOVE_100.length, pal);
    ctx.fillText(LOVE_100[i], 0, 0);
    ctx.restore();
  }

  const beat = Math.pow(Math.sin(frame * 0.11), 2);
  const coreR = 114 + beat * 3.5;
  ctx.beginPath();
  ctx.arc(cx, cy, coreR, 0, Math.PI * 2);
  ctx.fillStyle = toRgb(pal.centerFill);
  ctx.fill();
  ctx.strokeStyle = toRgb(pal.ringInner);
  ctx.lineWidth = 2;
  ctx.stroke();

  ctx.fillStyle = starCol;
  ctx.font = "bold 11px Georgia, serif";
  ctx.fillText("100 WAYS TO SAY", cx, cy - 50);
  ctx.fillText("I LOVE YOU ♥", cx, cy - 35);

  const badge = visibleCount > 0 ? `#${String(spotlightIdx + 1).padStart(2, "0")}` : "#00";
  ctx.fillStyle = outerCol;
  ctx.font = "bold 12px Consolas, monospace";
  ctx.fillText(badge, cx, cy - 15);

  const cursor = typedChars < targetCenterMsg.length && Math.floor(frame / 6) % 2 === 0 ? "|" : "";
  const shownMsg = targetCenterMsg.slice(0, typedChars) + cursor;
  ctx.fillStyle = toRgb(pal.textMain);
  ctx.font = "italic bold 14px Georgia, serif";
  const wrapped = wrapText(shownMsg, 185);
  const lineHeight = 18;
  const startY = cy + 12 - ((wrapped.length - 1) * lineHeight) / 2;
  wrapped.forEach((line, idx) => {
    ctx.fillText(line, cx, startY + idx * lineHeight);
  });

  ctx.fillStyle = toRgb(pal.c2);
  ctx.font = "bold 11px Consolas, monospace";
  ctx.fillText(`${visibleCount} / ${LOVE_100.length}`, cx, cy + 52);

  angleOffset = (angleOffset + 0.35) % 360;
  orbitAngle = (orbitAngle + 0.7) % 360;
  themeProgress = (themeProgress + 0.0022) % THEMES.length;
  frame++;

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);