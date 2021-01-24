notes = []
chords = []

def play_chord(chord):
    #Altera os valores das notas de acordo com o acorde tocado
    a = chord[0]
    b = chord[1]
    chord_played = notes[a:b]
    chord = most_frequent(chord_played)

    for key, note in enumerate(notes):
        if key >= a and key <=b:
            notes[key] = (note + chord) % 9

def most_frequent(list):
    #Retorna o valor que mais aparece em uma dada lista
    return max(set(list), key = list.count)

def play_chords(list):
    #Toca cada acorde sequencialmente
    for chord in list:
        play_chord(chord)

def getChords(q):
    #Pega da entrada os acordes tocados
    list_chords = []
    for i in range(q):
        try:
            a, b = input().split()
        except ValueError:
            print ("Número inválido")        
        list_chords += [(int(a),int(b))]
    return list_chords


try:
    n, q = input().split()

    notes = [1] * int(n)
    chords = getChords(int(q))
    
    play_chords(chords)

    for note in notes:
        print(note)

except ValueError:
    print ("Número inválido")
