from flask import Flask, render_template, request, jsonify
import subprocess
import os
import uuid

app = Flask(__name__)
EXPERIMENTS = {
    "1": {
        "aim": "To convert temperature from Celsius to Fahrenheit.",
        "algorithm": """
1. Read temperature in Celsius.
2. Apply formula F = (C × 9/5) + 32.
3. Display temperature in Fahrenheit.
""",
        "code": """#include <stdio.h>
int main() {
    float c, f;
    printf("Enter temperature in Celsius: ");
    scanf("%f", &c);
    f = (c * 9 / 5) + 32;
    printf("Temperature in Fahrenheit = %.2f", f);
    return 0;
}
"""
    },

    "2": {
        "aim": "To find the roots of a quadratic equation.",
        "algorithm": """
1. Read coefficients a, b, c.
2. Calculate discriminant d = b² − 4ac.
3. Find roots based on discriminant value.
4. Display the roots.
""",
        "code": """#include <stdio.h>
#include <math.h>
int main() {
    float a, b, c, d, r1, r2;
    printf("Enter a, b and c: ");
    scanf("%f %f %f", &a, &b, &c);
    d = b*b - 4*a*c;
    if(d > 0) {
        r1 = (-b + sqrt(d)) / (2*a);
        r2 = (-b - sqrt(d)) / (2*a);
        printf("Roots are %.2f and %.2f", r1, r2);
    } else if(d == 0) {
        r1 = -b / (2*a);
        printf("Root is %.2f", r1);
    } else {
        printf("Roots are imaginary");
    }
    return 0;
}
"""
    },
    "3": {
"aim": "To check whether a given number is prime or not.",
"algorithm": """
1. Read an integer n.
2. If n <= 1, it is not prime.
3. Check divisibility from 2 to n/2.
4. If divisible, not prime; else prime.
""",
"code": """#include <stdio.h>
int main() {
    int n, i, flag = 1;
    printf("Enter a number: ");
    scanf("%d", &n);

    if(n <= 1) flag = 0;
    for(i = 2; i <= n/2; i++) {
        if(n % i == 0) {
            flag = 0;
            break;
        }
    }

    if(flag)
        printf("%d is a prime number", n);
    else
        printf("%d is not a prime number", n);
    return 0;
}
"""
},

"4": {
"aim": "To search a key element in an array using linear search.",
"algorithm": """
1. Read number of elements.
2. Read array elements.
3. Read key element.
4. Compare key with each element.
5. Display result.
""",
"code": """#include <stdio.h>
int main() {
    int a[50], n, key, i, found = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements: ");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Enter key: ");
    scanf("%d", &key);

    for(i = 0; i < n; i++) {
        if(a[i] == key) {
            found = 1;
            break;
        }
    }

    if(found)
        printf("Element found at position %d", i + 1);
    else
        printf("Element not found");
    return 0;
}
"""
},

"5": {
"aim": "To categorize a person as senior citizen based on age and gender.",
"algorithm": """
1. Read age and gender.
2. If age >= 60, senior citizen.
3. Else, not senior citizen.
""",
"code": """#include <stdio.h>
int main() {
    int age;
    char gender;
    printf("Enter age and gender (M/F): ");
    scanf("%d %c", &age, &gender);

    if(age >= 60)
        printf("Senior Citizen");
    else
        printf("Not a Senior Citizen");
    return 0;
}
"""
},

"6": {
"aim": "To generate Floyd's Triangle for given number of rows.",
"algorithm": """
1. Read number of rows.
2. Print numbers sequentially in triangular form.
""",
"code": """#include <stdio.h>
int main() {
    int n, i, j, num = 1;
    printf("Enter number of rows: ");
    scanf("%d", &n);

    for(i = 1; i <= n; i++) {
        for(j = 1; j <= i; j++) {
            printf("%d ", num++);
        }
        printf("\\n");
    }
    return 0;
}
"""
},

"7": {
"aim": "To find the transpose of a matrix.",
"algorithm": """
1. Read matrix size.
2. Read matrix elements.
3. Display transpose.
""",
"code": """#include <stdio.h>
int main() {
    int a[10][10], i, j, r, c;
    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);

    printf("Enter matrix elements: ");
    for(i = 0; i < r; i++)
        for(j = 0; j < c; j++)
            scanf("%d", &a[i][j]);

    printf("Transpose:\\n");
    for(j = 0; j < c; j++) {
        for(i = 0; i < r; i++)
            printf("%d ", a[i][j]);
        printf("\\n");
    }
    return 0;
}
"""
},

"8": {
"aim": "To perform string operations using built-in functions.",
"algorithm": """
1. Read two strings.
2. Find length, copy, and concatenate strings.
""",
"code": """#include <stdio.h>
#include <string.h>
int main() {
    char s1[50], s2[50];
    printf("Enter first string: ");
    scanf("%s", s1);
    printf("Enter second string: ");
    scanf("%s", s2);

    printf("Length of first string = %lu\\n", strlen(s1));
    strcpy(s2, s1);
    printf("Copied string = %s\\n", s2);
    strcat(s1, s2);
    printf("Concatenated string = %s", s1);
    return 0;
}
"""
},

"9": {
"aim": "To find GCD and LCM using modular functions.",
"algorithm": """
1. Read two numbers.
2. Use function to compute GCD.
3. Compute LCM.
""",
"code": """#include <stdio.h>
int gcd(int a, int b) {
    if(b == 0) return a;
    return gcd(b, a % b);
}
int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    int g = gcd(a, b);
    printf("GCD = %d\\nLCM = %d", g, (a*b)/g);
    return 0;
}
"""
},

"10": {
"aim": "To display employee details with higher salary.",
"algorithm": """
1. Define structure.
2. Read two employee details.
3. Compare salaries.
""",
"code": """#include <stdio.h>
struct emp {
    int id;
    float salary;
};
int main() {
    struct emp e1, e2;
    printf("Enter id and salary of emp1: ");
    scanf("%d %f", &e1.id, &e1.salary);
    printf("Enter id and salary of emp2: ");
    scanf("%d %f", &e2.id, &e2.salary);

    if(e1.salary > e2.salary)
        printf("Employee %d has higher salary", e1.id);
    else
        printf("Employee %d has higher salary", e2.id);
    return 0;
}
"""
},

"11": {
"aim": "To add two numbers using pointers.",
"algorithm": """
1. Read two numbers.
2. Use pointers to add them.
""",
"code": """#include <stdio.h>
int main() {
    int a, b, sum;
    int *p1, *p2;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    p1 = &a;
    p2 = &b;
    sum = *p1 + *p2;
    printf("Sum = %d", sum);
    return 0;
}
"""
},

"12": {
"aim": "To find the sum of digits of a given number.",
"algorithm": """
1. Read number.
2. Extract digits and sum.
""",
"code": """#include <stdio.h>
int main() {
    int n, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    while(n > 0) {
        sum += n % 10;
        n /= 10;
    }
    printf("Sum of digits = %d", sum);
    return 0;
}
"""
},

"13": {
"aim": "To perform matrix multiplication.",
"algorithm": """
1. Read matrices.
2. Multiply using nested loops.
""",
"code": """#include <stdio.h>
int main() {
    int a[5][5], b[5][5], c[5][5] = {0};
    int i, j, k, r, c1;
    printf("Enter order of matrix: ");
    scanf("%d %d", &r, &c1);

    printf("Enter matrix A: ");
    for(i=0;i<r;i++)
        for(j=0;j<c1;j++)
            scanf("%d",&a[i][j]);

    printf("Enter matrix B: ");
    for(i=0;i<r;i++)
        for(j=0;j<c1;j++)
            scanf("%d",&b[i][j]);

    for(i=0;i<r;i++)
        for(j=0;j<c1;j++)
            for(k=0;k<c1;k++)
                c[i][j] += a[i][k] * b[k][j];

    printf("Result:\\n");
    for(i=0;i<r;i++) {
        for(j=0;j<c1;j++)
            printf("%d ", c[i][j]);
        printf("\\n");
    }
    return 0;
}
"""
},

"14": {
"aim": "To store book details and search a specific book.",
"algorithm": """
1. Define structure.
2. Read book details.
3. Search by title.
""",
"code": """#include <stdio.h>
#include <string.h>
struct book {
    char title[30];
};
int main() {
    struct book b[3];
    char key[30];
    int i, found = 0;

    printf("Enter book titles:\\n");
    for(i=0;i<3;i++)
        scanf("%s", b[i].title);

    printf("Enter book to search: ");
    scanf("%s", key);

    for(i=0;i<3;i++) {
        if(strcmp(b[i].title, key) == 0) {
            found = 1;
            break;
        }
    }

    if(found)
        printf("Book is available");
    else
        printf("Book not available");
    return 0;
}
"""
}
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/experiment/<exp_id>")
def experiment(exp_id):
    if exp_id not in EXPERIMENTS:
        return "Experiment not found"

    exp = EXPERIMENTS[exp_id]

    return render_template(
        "experiment.html",
        exp_id=exp_id,
        aim=exp["aim"],
        algorithm=exp["algorithm"],
        code=exp["code"]
    )


""" @app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    user_input = request.form.get('input', '')

    job_id = uuid.uuid4().hex
    #job_dir = f"/tmp/{job_id}"
    job_dir = os.path.abspath(f"temp/{job_id}")
    os.makedirs(job_dir, exist_ok=True)
    print("Job dir:", job_dir)
    print("Files:", os.listdir(job_dir))

    with open(f"{job_dir}/program.c", "w") as f:
        f.write(code)

    with open(f"{job_dir}/input.txt", "w") as f:
        f.write(user_input)

    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{job_dir}:/code",
        "--network", "none",
        "--memory", "64m",
        "--cpus", "0.5",
        "c_vlab_image"
    ]

    try:
        result = subprocess.run(
            docker_cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = "Execution timed out"

    os.system(f"rm -rf {job_dir}")

    return jsonify({"output": output}) """
@app.route("/run", methods=["POST"])
def run():
    exp_id = request.form["exp_id"]
    exp = EXPERIMENTS.get(exp_id)

    if not exp:
        return "Invalid experiment"

    input_data = request.form.get("input_data", "")

    job_id = uuid.uuid4().hex
    job_dir = os.path.join("temp", job_id)
    os.makedirs(job_dir, exist_ok=True)

    with open(os.path.join(job_dir, "program.c"), "w") as f:
        f.write(exp["code"])

    with open(os.path.join(job_dir, "input.txt"), "w") as f:
        f.write(input_data)

    cmd = [
        "bash", "-c",
        "gcc program.c -o program -lm 2> compile_error.txt && "
        "./program < input.txt"
    ]

    try:
        result = subprocess.check_output(
            cmd,
            cwd=job_dir,                 # 🔥 FIX
            stderr=subprocess.STDOUT,
            text=True,
            timeout=5
        )
    except subprocess.CalledProcessError as e:
        result = e.output
    except subprocess.TimeoutExpired:
        result = "Error: Program execution timed out."

    print("PROGRAM OUTPUT:", result)

    return render_template(
        "experiment.html",
        exp_id=exp_id,
        aim=exp["aim"],
        algorithm=exp["algorithm"],
        code=exp["code"],
        output=result
    )


if __name__ == '__main__':
    app.run(debug=True)
