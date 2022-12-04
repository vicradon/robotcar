
int delay_time = 500;
int pin = 13;

void init()
{
    pinMode(pin, OUTPUT);
}

void loop()
{
    digitalWrite(pin, HIGH);
    delay(delay_time);
    digitalWrite(pin, LOW);
    delay(delay_time);
}