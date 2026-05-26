{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lannessuellen-pixel/exemplo/blob/main/notebooks/sem2_exer_fixacao_7.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lado1 = int(input(\"Digite o lado 1 do triângulo: \"))\n",
        "lado2 = int(input(\"Digite o lado 2 do triângulo: \"))\n",
        "lado3 = int(input(\"Digite o lado 3 do triângulo: \"))\n",
        "\n",
        "if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:\n",
        "  print(\"Isso não é um triângulo\")\n",
        "else:\n",
        "  if lado1 == lado2 == lado3:\n",
        "    print(\"Isso é um triângulo equilátero\")\n",
        "  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:\n",
        "    print(\"Isso é um triângulo isósceles\")\n",
        "  else:\n",
        "    print(\"Isso é um triângulo escaleno\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S6wS3R5EN1Eh",
        "outputId": "182491b6-b82e-4464-f08b-e71f76669455"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o lado 1 do triângulo: 5\n",
            "Digite o lado 2 do triângulo: 5\n",
            "Digite o lado 3 do triângulo: 3\n",
            "Isso é um triângulo isósceles\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "generative_ai_disabled": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}