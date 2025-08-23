// [dependencies]
// rdev = "0.5.3"
use rdev::{listen, Event, EventType};

fn main() {
    println!("开始监听键盘/鼠标事件...");

    listen(|event: Event| {
        match event.event_type {
            EventType::KeyPress(key) => {
                println!("⌨️ 按下: {:?}", key);
            }
            EventType::ButtonPress(button) => {
                println!("🖱️ 点击: {:?}", button);
            }
            _ => {}
        }
    }).expect("无法启动监听");
}
