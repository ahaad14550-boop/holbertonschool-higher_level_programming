const size = parseInt(process.argv[2]);

#!/usr/bin/node
if (isNaN(size)) {
    console.log("Missing size");
} else {
    // الحلقة الأولى: مسؤولة عن تكرار الأسطر (الارتفاع)
    for (let i = 0; i < size; i++) {
        let row = ''; // 1. نبدأ بمتغير نصي فارغ لكل سطر جديد

        // الحلقة الثانية: مسؤولة عن بناء السطر الواحد بالعرض
        for (let j = 0; j < size; j++) {
            row += 'X'; // 2. نضيف حرف X في كل مرة داخل السطر
        }

        // 3. نطبع السطر المكتمل بعد انتهاء الحلقة الداخلية
        console.log(row);
    }
}