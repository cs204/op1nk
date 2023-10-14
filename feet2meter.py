def main():
    v = input("Сколько футов:")
    value, unit = v.split('ft')
    v = feet2meter(float(value))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
  return v * 0.3048

main()