package sistema;

import java.util.ArrayList;
import java.util.Scanner;

public class Alunos {

    static ArrayList<String> nomes = new ArrayList<>();
    static ArrayList<Double> medias = new ArrayList<>();
    static ArrayList<String> resultados = new ArrayList<>();

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        cadastrarAlunos(sc);

        gerarRelatorio();

        sc.close();
    }

    public static void cadastrarAlunos(Scanner sc) {

        int contador = 0;

        while (contador < 5) {

            System.out.print("Digite o nome do aluno: ");
            String nome = sc.nextLine();

            double media = calcularMedia(sc);

            String resultado = verificarResultado(media);

            nomes.add(nome);
            medias.add(media);
            resultados.add(resultado);

            contador++;
        }
    }

    public static double calcularMedia(Scanner sc) {

        int contadorNota = 0;

        double soma = 0;

        while (contadorNota < 3) {

            System.out.print("Digite a nota: ");
            double nota = sc.nextDouble();

            soma += nota;

            contadorNota++;
        }

        sc.nextLine();

        return soma / 3;
    }

    public static String verificarResultado(double media) {

        if (media >= 7) {
            return "Aprovado";
        } else if (media > 3 && media < 7) {
            return "Recuperação";
        } else {
            return "Reprovado";
        }
    }

    public static void gerarRelatorio() {

        System.out.println("\n===== RELATÓRIO FINAL =====");

        int contador = 0;

        while (contador < nomes.size()) {

            System.out.println("\nAluno: " + nomes.get(contador));

            System.out.printf("Média: %.2f%n", medias.get(contador));

            System.out.println("Resultado: " + resultados.get(contador));

            contador++;
        }
    }
}