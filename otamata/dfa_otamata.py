class DFA:
    def __init__(self, states, girdi, transition_function, baslangıc_state, kabul_states):
        self.states = states
        self.girdi = girdi
        self.transition_function = transition_function
        self.baslangıc_state = baslangıc_state
        self.kabul_states = kabul_states

    def simulate(self, giris_string):
        bulunan_state = self.baslangıc_state
        print(f"DFA simülasyonu başlatılıyor. Şuanki state: {bulunan_state}")

        for sembol in giris_string:
            if sembol not in self.girdi:
                print(f"Error: yanlış sembolü girdiniz: '{sembol}' DFA kabul sembollerinde yok.")
                return False

            bulunan_state = self.transition_function[bulunan_state][sembol]
            print(f"Okunan sembol: '{sembol}', Şuanki state: {bulunan_state}")

        if bulunan_state in self.kabul_states:
            print(f"String kabul edildi. Son state: {bulunan_state}  Kabul state i.")
            return True
        else:
            print(f"String Red. Son state: {bulunan_state} Kabul state i değil.")
            return False

states_A = {"q0", "q1", "q2"}
girdi_A = {"a", "b"}
transition_function_A = {
    "q0": {"a": "q1", "b": "q0"},
    "q1": {"a": "q2", "b": "q0"},
    "q2": {"a": "q2", "b": "q2"},
}
baslangıc_state_A = "q0"
kabul_states_A = {"q0", "q1"}

dfa_A = DFA(states_A, girdi_A, transition_function_A, baslangıc_state_A, kabul_states_A)

states_B = {"q0", "q1", "q2", "q3"}
girdi_B = {"a", "b"}
transition_function_B = {
    "q0": {"a": "q1", "b": "q3"},
    "q1": {"a": "q1", "b": "q2"},
    "q2": {"a": "q3", "b": "q2"},
    "q3": {"a": "q3", "b": "q3"},
}
baslangıc_state_B = "q0"
kabul_states_B = {"q0", "q2"}

dfa_B = DFA(states_B, girdi_B, transition_function_B, baslangıc_state_B, kabul_states_B)

states_C = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"}
girdi_C = {"a", "b"}
transition_function_C = {
    "q0": {"a": "q1", "b": "q3"},
    "q1": {"a": "q2", "b": "q4"},
    "q2": {"a": "q1", "b": "q5"},
    "q3": {"a": "q4", "b": "q6"},
    "q4": {"a": "q5", "b": "q7"},
    "q5": {"a": "q4", "b": "q8"},
    "q6": {"a": "q7", "b": "q3"},
    "q7": {"a": "q8", "b": "q4"},
    "q8": {"a": "q5", "b": "q7"},
}
baslangıc_state_C = "q0"
kabul_states_C = {"q8"}

dfa_C = DFA(states_C, girdi_C, transition_function_C, baslangıc_state_C, kabul_states_C)

print("Test etmek için bir dil seçin:")
print("1. Dil A: 'a' ve 'b' harflerinden oluşan, ardışık iki 'aa' içermeyen tüm dizgeler.")
print("2. Dil B: Boş dizge veya 'a' ile başlayıp 'b' ile biten tüm dizgeler.")
print("3. Dil C: En az iki 'a' ve iki 'b' içeren tüm dizgeler.")

choice = input("Seçim Yapın (1/2/3): ")
if choice == "1":
    dfa = dfa_A
elif choice == "2":
    dfa = dfa_B
elif choice == "3":
    dfa = dfa_C
else:
    print("Olmayan bir dili seçtiniz programı tekrar başlatın.")
    dfa = None

if dfa:
    for i in range(4):
        giris_string = input(f"String girin {i + 1} test için: ")
        result = dfa.simulate(giris_string)
        print("Kabul" if result else "Red")
        if i == 3:
            print("Simülasyon tamamlandı.")


